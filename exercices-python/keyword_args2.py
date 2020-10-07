def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print('-- I am sorry, we are all ou of', kind)

    for arg in arguments:
        print(arg)

    print('-' * 40)

    for kw in keywords:
        print(kw, ':', keywords[kw])

cheeseshop(
    'Limburger',
    'It is very runny, sir',
    'It is really very runny, sir',
    shopkeeper = 'Michael Palin',
    client = 'John Cleese',
    sketch = 'Cheese Shop Sketch'
)
