from sys import stdin

boards = []
numbers = []

def readBoards():
    global numbers

    numbers = [int(x) for x in stdin.readline().strip().split(",")]

    blankLine = stdin.readline().strip()

    a = stdin.readline().strip().split()

    while a:

        board = []
        
        board.append([int(x) for x in a])

        for i in range(4):
            board.append([int(x) for x in stdin.readline().strip().split()])

        # for i in board:
        #     print(i)

        boards.append(board)

        blankLine = stdin.readline().strip()
        a = stdin.readline().strip().split()

    # for i in boards:
    #     for j in i:
    #         print(j)
    #     print()


def sumUnMarked(boardNumber):
    
    sum = 0

    for i in range(5):
        for j in range(5):

            if(boards[boardNumber][i][j] > 0):
                sum += boards[boardNumber][i][j]
    
    return sum

def markAndCheckBoard(boardNumber, number):

    for i in range(5):
        for j in range(5):
            
            if(boards[boardNumber][i][j] == number):
                boards[boardNumber][i][j] += 1
                boards[boardNumber][i][j] *= -1
        
    for i in range(5):

        horizontal = 0
        vertical = 0

        for j in range(5):

            if(boards[boardNumber][i][j] < 0):
                horizontal += 1

            if(boards[boardNumber][j][i] < 0):
                vertical += 1
            
        if(vertical == 5 or horizontal == 5):
            result = sumUnMarked(boardNumber)        
            return result * number

    return -1

def main():
    
    readBoards()
    
    winnerBoards = [0] * len(boards)
    
    for i in range(len(numbers)):

        # print(numbers[i])
        # print(winnerBoards)
        # for y in boards:
        #     for x in y:
        #         print(x)
        #     print()

        for j in range(len(boards)):

            if(winnerBoards[j] == 1): continue

            res = markAndCheckBoard(j, numbers[i])

            if(res > 0):
                winnerBoards[j] = 1

                # let's wait until the last one wins
                if(sum(winnerBoards) == len(boards)):
                    print(res)
                    return

                res = -1
            
main()