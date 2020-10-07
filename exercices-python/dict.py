tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

del tel['sape']
print(tel)

tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(tel.keys())

print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)