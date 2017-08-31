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

for _ in board:
    _.append(' . '*10)

def show_board(board_in):
    for row in board_in:
        print("".join((str(x) for x in row)))

def main():
    print('Welcome to battleship v0.01!')
    show_board(board)
    game_ended = False
    while not game_ended:
        print(input('Guess: '))

main()