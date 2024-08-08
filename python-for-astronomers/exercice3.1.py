import os

import matplotlib.pyplot as plt
import numpy as np

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spectrum.txt")
data = np.loadtxt(file_path)
data = np.transpose(data)
data = np.loadtxt(file_path, unpack=tr)
# plt.plot(*data)
fluxes, wavelength = data
plt.plot(fluxes, wavelength)
plt.show()
