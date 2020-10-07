def ask_ok(prompt: str, retries = 4, reminder = 'Please try again!') -> bool:
    while True:
        ok = input(prompt)

        if ok in ('y', 'ye', 'yes'):
            return True

        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1

        if retries < 0:
            raise ValueError('invalid user response')

        print(reminder)

print(ask_ok('do you really want to quit?'))
