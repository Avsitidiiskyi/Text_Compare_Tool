from random import randint

from pip._vendor.distlib.compat import raw_input
print("----СВИСТАТЬ ВСЕЕЕХ НАВЕЕЕРХ-----")
board = []

for i in range(0, 10):
    board.append(['O'] * 10)  # iteration to create battlefield


def print_board(board):  # func+argument to create 10 rows in table.
    for row in board:
        print(" ".join(row))  # join is used to split elements with (" ") empty spaces.


print(print_board(board))


def gam_over():
    print('Нет, мой капитан! Все мимо, пошли бухать!')
def gam_win():
    print('Все, Капитан! Мы победили. Пошли бухать! ')
def tuppizza():
    print("Ты уже палил туда, тупица!")
def kkkombo():
    result = (gam_over(), tuppizza())
    return result



def horizon(board):
    a = randint(0, len(board) - 1)
    return a


def vertical(board):
    a = randint(0, len(board) - 1)
    return a


ship_raw = horizon(board)
ship_col = vertical(board)

#print(ship_raw) #- print to see actual randint result
#print(ship_col)# - print to see actual randint result

for charge in range(4):
    print('Выстрел', charge + 1)
    guess_row = int(raw_input('Капитан! Введите координаты Х для атаки: '))
    guess_col = int(raw_input('Теперь координаты У для атаки: '))

    if guess_row == ship_raw and guess_col == ship_col:
        print("Есть попадание!!!")
        board[guess_row][guess_col] = "K"
        gam_win()
        break


    else:
        if guess_row not in range(0, 10) or guess_col not in range(0, 10):
            #(guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10): - alternative
            print("\n \n Мой капитан, бухать нужно меньше!\n Ты ж, говядина такая, даже в корабль в подзорную трубу не видишь!!!! ")

        elif (board[guess_row][guess_col] == "X"):
            tuppizza()
        else:
            print("Мимо!")
            if charge == 3:
                gam_over()

    if charge == 3 and (board[guess_row][guess_col] == "X"):
        kkkombo()




    board[guess_row][guess_col] = "X"
    print_board(board)



    # to improve:
    # try - except for  out of range error
    # game over function doesn't work
    # cosider "while" cycle for non int values during coordinates definition
    # remove visual random input before first turn (Done)








