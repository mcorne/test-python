knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(knights.items())
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? Is it {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = 'apple', 'orange', 'apple', 'pear', 'orange', 'banana'
print(sorted(basket))
print(basket)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
