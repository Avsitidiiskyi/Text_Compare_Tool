RED = '\033[0;31m'
GREEN = '\033[0;36m'
expected = input('Enter expected text:')
actual = input('Enter actual text:')

def compare():
    if len(expected) < len(actual):
        min_range = len(expected)
    else:
        min_range = len(actual)

    for i in range(min_range):
        if expected[i] != actual[i]:
            print(f'Error from index - {i}')
            print(expected)
            print(actual[:i] + RED + actual[i:])
            break


if expected == actual:
    print(GREEN + 'TEXT IS EQUAL')

print(compare())


