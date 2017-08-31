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

for row in board:
    row.append([False]*10)

def main():
    print('Welcome to battleship v0.01!')
    for row in board:
        for value in row:
            #print(value, end='')

main()