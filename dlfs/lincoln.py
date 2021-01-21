import os
import pickle
from copy import deepcopy
from typing import List, Tuple

import numpy as np
from numpy import ndarray
from scipy.special import softmax


def load():
    with open("mnist.pkl",'rb') as f:
        mnist = pickle.load(f)
    return mnist["training_images"], mnist["training_labels"], mnist["test_images"], mnist["test_labels"]

def assert_same_shape(array: ndarray, array_grad: ndarray):
    assert array.shape == array_grad.shape, f"array and grad shapes do not match:  {array.shape} != {array_grad.shape}"

def mae(y_true: ndarray, y_pred: ndarray): # mean absolute error
    return np.mean(np.abs(y_true - y_pred))

def normalize(a: np.ndarray):
    other = 1 - a
    return np.concatenate([a, other], axis=1)

def rmse(y_true: ndarray, y_pred: ndarray): # root mean squared error
    return np.sqrt(np.mean(np.power(y_true - y_pred, 2)))

def permute_data(X, y):
    perm = np.random.permutation(X.shape[0])
    return X[perm], y[perm]

def to_2d_np(a: ndarray, type: str="col") -> ndarray: # convert 1D Tensor into 2D
    assert a.ndim == 1, "Input tensors must be 1 dimensional"
    if type == "col":
        return a.reshape(-1, 1)
    elif type == "row":
        return a.reshape(1, -1)

def unnormalize(a: np.ndarray):
    return a[np.newaxis, 0]

class Operation:
    def forward(self, input_:ndarray, inference: bool=False):
        self.input_ = input_
        self.output = self._output(inference)
        return self.output

    def backward(self, output_grad: ndarray) -> ndarray:
        assert_same_shape(self.output, output_grad)
        self.input_grad = self._input_grad(output_grad)
        assert_same_shape(self.input_, self.input_grad)
        return self.input_grad

    def _output(self, inference: bool) -> ndarray:
        raise NotImplementedError

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        raise NotImplementedError

class ParamOperation(Operation):
    def __init__(self, param: ndarray):
        self.param = param

    def backward(self, output_grad: ndarray) -> ndarray:
        super().backward(output_grad)
        self.param_grad = self._param_grad(output_grad)
        assert_same_shape(self.param, self.param_grad)
        return self.input_grad

    def _param_grad(self, output_grad: ndarray) -> ndarray:
        raise NotImplementedError

class WeightMultiply(ParamOperation):
    def __init__(self, W: ndarray):
        super().__init__(W)

    def _output(self, inference: bool) -> ndarray:
        return np.dot(self.input_, self.param)

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return np.dot(output_grad, np.transpose(self.param))

    def _param_grad(self, output_grad: ndarray) -> ndarray:
        return np.dot(np.transpose(self.input_), output_grad)

class BiasAdd(ParamOperation):
    def __ini__(self, B: ndarray):
        assert B.shape[0] == 1
        super().__init__(B)

    def _output(self, inference: bool) -> ndarray:
        return self.input_ + self.param

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return np.ones_like(self.input_) * output_grad

    def _param_grad(self, output_grad: ndarray) -> ndarray:
        param_grad = np.ones_like(self.param) * output_grad
        return np.sum(param_grad, axis=0).reshape(1, -1)

class Linear(Operation):
    def _output(self, inference: bool) -> ndarray:
        return self.input_

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return output_grad

class Sigmoid(Operation):
    def _output(self, inference: bool) -> ndarray:
        return 1 / (1 + np.exp(-1 * self.input_))

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        sigmoid_backward = self.output * (1 - self.output)
        return sigmoid_backward * output_grad

class Tanh(Operation):
    def _output(self, inference: bool) -> ndarray:
        return np.tanh(self.input_)

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return output_grad * (1 - self.output * self.output)


class Layer:
    def __init__(self, neurons: int):
        self.neurons = neurons
        self.first = True
        self.params = []
        self.param_grads = []
        self.operations = []
        self.seed = None

    def _setup_layer(self, num_in: int):
        raise NotImplementedError

    def forward(self, input_: ndarray, inference=False) -> ndarray:
        if self.first:
            self._setup_layer(input_)
            self.first = False
        self.input_ = input_
        for operation in self.operations:
            input_ = operation.forward(input_, inference)
        self.output = input_
        return self.output

    def backward(self, output_grad: ndarray) -> ndarray:
        assert_same_shape(self.output, output_grad)
        for operation in reversed(self.operations):
            output_grad = operation.backward(output_grad)
        input_grad = output_grad
        assert_same_shape(self.input_, input_grad)
        self._param_grads()
        return input_grad

    def _param_grads(self) -> ndarray:
        self.param_grads = []
        for operation in self.operations:
            if issubclass(operation.__class__,ParamOperation):
                self.param_grads.append(operation.param_grad)

class Dense(Layer):
    def __init__(self, neurons: int, activation: Operation = Sigmoid(), conv_in=False, dropout=1.0, weight_init="standard"):
        super().__init__(neurons)
        self.activation = activation
        self.conv_in = conv_in
        self.dropout = dropout
        self.weight_init = weight_init

    def _setup_layer(self, input_: ndarray):
        if self.seed:
            np.random.seed(self.seed)
        num_in = input_.shape[1]
        if self.weight_init == "glorot":
            scale = 2/(num_in + self.neurons)
        else:
            scale = 1.0
        self.params = []
        self.params.append(np.random.normal(loc=0, scale=scale, size=(num_in, self.neurons))) # weights
        self.params.append(np.random.normal(loc=0, scale=scale, size=(1, self.neurons))) # bias
        self.operations = [WeightMultiply(self.params[0]), BiasAdd(self.params[1]), self.activation]

class Loss:
    def forward(self, prediction: ndarray, target: ndarray) -> float:
        assert_same_shape(prediction, target)
        self.prediction = prediction
        self.target = target
        loss_value = self._output()
        return loss_value

    def backward(self) -> ndarray:
        self.input_grad = self._input_grad()
        assert_same_shape(self.prediction, self.input_grad)
        return self.input_grad

    def _output(self) -> float:
        raise NotImplementedError

    def _input_grad(self) -> ndarray:
        raise NotImplementedError

class MeanSquaredError(Loss):
    def __init__(self, normalize: bool = False) -> None:
        self.normalize = normalize

    def _output(self) -> float:
        if self.normalize:
            self.prediction = self.prediction / self.prediction.sum(axis=1, keepdims=True)
        loss = np.sum(np.power(self.prediction - self.target, 2)) / self.prediction.shape[0]
        return loss

    def _input_grad(self) -> ndarray:
        return 2 * (self.prediction - self.target) / self.prediction.shape[0]

class SoftmaxCrossEntropy(Loss):
    def __init__(self, eps=1e-9):
        self.eps = eps
        self.single_class = False

    def _output(self)-> float:
        if self.target.shape[1] == 0:
            self.single_class = True
        if self.single_class:
            self.prediction, self.target = normalize(self.prediction), normalize(self.target)
        softmax_preds = softmax(self.prediction, axis=1)
        self.softmax_preds = np.clip(softmax_preds, self.eps, 1 - self.eps)
        softmax_cross_entropy_loss = -self.target * np.log(self.softmax_preds) - (1 - self.target) * np.log(1 - self.softmax_preds)
        return np.sum(softmax_cross_entropy_loss) / self.prediction.shape[0]

    def _input_grad(self):
        if self.single_class:
            return unnormalize(self.softmax_preds - self.target)
        else:
            return (self.softmax_preds - self.target) / self.prediction.shape[0]
class LayerBlock:
    def __init__(self, layers: List[Layer]):
        self.layers = layers

    def forward(self, X_batch: ndarray, inference=False) ->  ndarray:
        X_out = X_batch
        for layer in self.layers:
            X_out = layer.forward(X_out, inference)
        return X_out

    def backward(self, loss_grad: ndarray) -> ndarray:
        grad = loss_grad
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def params(self):
        for layer in self.layers:
            yield from layer.params

    def param_grads(self):
        for layer in self.layers:
            yield from layer.param_grads

    def __iter__(self):
        return iter(self.layers)

    def __repr__(self):
        layer_strs = [str(layer) for layer in self.layers]
        return f"{self.__class__.__name__}(\n  " + ",\n  ".join(layer_strs) + ")"

class NeuralNetwork(LayerBlock):
    def __init__(self, layers: List[Layer], loss: Loss, seed: float = 1):
        self.layers = layers
        self.loss = loss
        self.seed = seed
        if seed:
            for layer in self.layers:
                layer.seed = self.seed

    def forward_loss(self,  X_batch: ndarray,  y_batch: ndarray, inference: bool = False) -> float:
        prediction = self.forward(X_batch, inference)
        return self.loss.forward(prediction, y_batch)

    def train_batch(self, X_batch: ndarray, y_batch: ndarray, inference: bool = False) -> float:
        prediction = self.forward(X_batch, inference)
        batch_loss = self.loss.forward(prediction, y_batch)
        loss_grad = self.loss.backward()
        self.backward(loss_grad)
        return batch_loss

class Optimizer:
    def __init__(self, lr=0.01, final_lr=0, decay_type: str = None):
        self.lr = lr
        self.final_lr = final_lr
        self.decay_type = decay_type
        self.first = True

    def _setup_decay(self):
        if self.decay_type == "exponential":
            self.decay_per_epoch = np.power(self.final_lr / self.lr, 1 / (self.max_epochs - 1))
        elif self.decay_type == "linear":
            self.decay_per_epoch = (self.lr - self.final_lr) / (self.max_epochs - 1)

    def _decay_lr(self):
        if self.decay_type == "exponential":
            self.lr *= self.decay_per_epoch
        elif self.decay_type == "linear":
            self.lr -= self.decay_per_epoch

    def step(self, epoch=0):
        for param, param_grad in zip(self.net.params(), self.net.param_grads()):
            self._update_rule(param=param, grad=param_grad)

    def _update_rule(self, **kwargs):
        raise NotImplementedError

class SGD(Optimizer): # Stochastic gradient descent
    def _update_rule(self, **kwargs):
        kwargs["param"] -= self.lr * kwargs["grad"]

class SGDMomentum(Optimizer):
    def __init__(self, lr=0.01, final_lr=0, decay_type: str = None, momentum=0.9):
        super().__init__(lr, final_lr, decay_type)
        self.momentum = momentum

    def step(self):
        if self.first:
            self.velocities = [np.zeros_like(param) for param in self.net.params()]
            self.first = False
        for param, param_grad, velocity in zip(self.net.params(), self.net.param_grads(), self.velocities):
            self._update_rule(param=param, grad=param_grad, velocity=velocity)

    def _update_rule(self, **kwargs):
        kwargs["velocity"] *= self.momentum
        kwargs["velocity"] += self.lr * kwargs["grad"]
        kwargs["param"] -= kwargs["velocity"]

class Trainer:
    def __init__(self, net: NeuralNetwork, optim: Optimizer):
        self.net = net
        self.optim = optim
        self.optim.net = net
        self.best_loss = 1e9

    def generate_batches(self, X: ndarray, y: ndarray, size=32) -> Tuple[ndarray]:
        assert X.shape[0] == y.shape[0], f"features and targets number of rows do not match: {X.shape[0]} != {y.shape[0]}"
        N = X.shape[0]
        for ii in range(0, N, size):
            X_batch, y_batch = X[ii:ii+size], y[ii:ii+size]
            yield X_batch, y_batch

    def fit(self, X_train: ndarray, y_train: ndarray, X_test: ndarray, y_test: ndarray,
            epochs=50, eval_every=10, batch_size=32, seed=1,
            single_output=False, restart=True, early_stopping=True, conv_testing=False):
        self.optim.max_epochs = epochs
        self.optim._setup_decay()
        np.random.seed(seed)
        if restart:
            for layer in self.net.layers:
                layer.first = True
            self.best_loss = 1e9

        for e in range(epochs):
            if (e+1) % eval_every == 0:
                last_model = deepcopy(self.net)

            X_train, y_train = permute_data(X_train, y_train)
            batch_generator = self.generate_batches(X_train, y_train, batch_size)
            for X_batch, y_batch in batch_generator:
                self.net.train_batch(X_batch, y_batch)
                self.optim.step()

            if (e+1) % eval_every == 0:
                test_preds = self.net.forward(X_test)
                loss = self.net.loss.forward(test_preds, y_test)
                if loss < self.best_loss:
                    print(f"Validation loss after {e+1} epochs is {loss:.3f}")
                    self.best_loss = loss
                else:
                    print(f"Loss increased after epoch {e+1}, final loss was {self.best_loss:.3f}, using model from epoch {e+1-eval_every}")
                    self.net = last_model
                    self.optim.net = self.net
                    break

def eval_regression_model(model: NeuralNetwork, X_test: ndarray, y_test: ndarray):
    preds = model.forward(X_test)
    preds = preds.reshape(-1, 1)
    print("Mean absolute error: {:.2f}".format(mae(preds, y_test)))
    print()
    print("Root mean squared error {:.2f}".format(rmse(preds, y_test)))
