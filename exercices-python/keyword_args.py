def parrot(voltage: str, state = 'a stiff', action = 'voom', type = 'Norwegian Blue') -> str:
    print("-- This parrot wouldn't", action, end = ' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the ', type)
    print("-- It's", state, '!')

# parrot(20)
# parrot(voltage = 100, action  = 'voooom')
parrot('a million', 'bereft of life', 'jump')
