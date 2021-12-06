from sys import stdin


def main():

    operation = stdin.readline().strip()

    currentPos = [0,0]
    aim = 0

    while operation:

        op, pos = operation.split()

        pos = int(pos)

        if(op == "up"):
            aim -= pos

        if(op == "down"):
            aim += pos

        if(op == "forward"):
            currentPos[1] += pos
            currentPos[0] += aim * pos

        #print(currentPos, aim)
        operation = stdin.readline().strip()

    print(currentPos[0] * currentPos[1])

main()