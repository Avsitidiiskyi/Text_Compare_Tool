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


#X = '\033[44;33mactual[i:]\033[m' თავლლსლფლება


# expected = input('Enter expected text:')
# actual = input('Enter actual text:')
#
# def compare():
#     if len(expected) < len(actual):
#         min_range = len(expected)
#     else:
#         min_range = len(actual)
#
#     for i in range(min_range):
#         if expected[i] != actual[i]:
#             print(f'Error from index - {i}')
#             print(f'Expected text {expected[i]}')
#             print(f'Actual text {actual[i]}')
#
#             print(expected)
#             print('\033[1;31;40m'+ actual[i:] + '\033[0;37;40m \n')
#
#             break
# if expected == actual:
#     print('Text is equal ')
#
#
# print(compare())





