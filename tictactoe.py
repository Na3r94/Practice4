import random
import time



def show():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()

def check():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            print('Player 1 wins')
            print(f"Time: {sec}")
            exit()
    for i in range(3):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            print('Player 1 wins')
            print(f"Time: {sec}")
            exit()
    for i in range(3):
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            print('Player 2 wins')
            print(f"Time: {sec}")
            exit()
    for j in range(3):
        if game[0][j] == 'O' and game[1][j] == 'O' and game[2][j] == 'O':
            print('Player 2 wins')
            print(f"Time: {sec}")
            exit()
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X': 
        print('Player 1 wins')
        print(f"Time: {sec}")
        exit()
    if game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X': 
        print('Player 1 wins')
        print(f"Time: {sec}")
        exit()
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O': 
        print('Player 2 wins')
        print(f"Time: {sec}")
        exit()
    if game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        print('Player 2 wins')
        print(f"Time: {sec}")
        exit()
    

game = [['-' , '-' , '-'],
        ['-' , '-' , '-'],
        ['-' , '-' , '-']]

show()
print('1 - 1 Player')
print('2 - 2 Player')

while True:
    a = int(input())
    if a == 1 or a == 2:
        break
    else:
        print('error! Enter the correct number')

rond = 0
while True:
    sec = time.time()
    print('Player 1')
    rond +=1
    while True:
        row = int(input())
        col = int(input())

        if 0 <= row <= 2 and 0 <= col <=2:
            if game[row][col] == '-':
                game[row][col] = 'X'
                # ketabkhune color ru nemitunm ejra konm vali dastor bayad be in shekl bashe:
                # game[row][col] = termcolor.colored ('X' , color= "Yellow")
                break
            else:
                print('error!!! This cell is not empty')
        else:
            print('error!!! index out of range. try again')

    show()
    check()

    if a == 2:
        if rond == 5:
            print('Draw!!!')
            exit()
        print('Player 2')
        while True:
            row = int(input())
            col = int(input())

            if 0 <= row <= 2 and 0 <= col <=2:
                if game[row][col] == '-':
                    game[row][col] = 'O'
                    break
                else:
                    print('error!!! This cell is not empty')
            else:
                print('error!!! index out of range. try again')
        show()
        check()

    
    if a == 1:
        if rond == 5:
            print('Draw!!!')
            exit()
        print('Pc')
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)

            if 0 <= row <= 2 and 0 <= col <=2:
                if game[row][col] == '-':
                    game[row][col] = 'O'
                    break
                else:
                    print('error!!! This cell is not empty')
            else:
                print('error!!! index out of range. try again')
        show()
        check()
        if rond == 5:
            print('Draw!!!')
            exit()