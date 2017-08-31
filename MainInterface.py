try:
    input = raw_input
except NameError:
    pass

board = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

num2letter = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}

for _ in board:
    _.append(' . '*10)

def check_input(teststr):
    ##Checks if an input if valid, if so returns it, if not returns 'None'
    valid = False
    while not valid:
        str = input(teststr)
        try:
            if not str[0].isalpha():
                raise Exception
            if not len(str) == 2:
                raise Exception
            test_int = int(str[1])

            ##String is good
            valid = True
            return num2letter[0]+str[1]
        except:
            print('Invalid Input! \n')

def show_board(board_in):
    for row in board_in:
        print("".join((str(x) for x in row)))

def main():
    print('Welcome to battleship v0.01!')
    show_board(board)
    game_ended = False
    while not game_ended:
        print(check_input('Guess: '))
        #print('test')

main()