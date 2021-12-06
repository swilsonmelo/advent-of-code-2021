from sys import stdin
import math



def main():

    numbers = []

    a = stdin.readline().strip()

    while a:
        a = int(a)

        numbers.append(a)
        
        a = stdin.readline().strip()


    count = 0

    first = 0
    for i in range(3):
        first += numbers[i]

    for i in range(1, len(numbers)-2):
        second = 0
        for j in range(3):
            second += numbers[i + j]
        if(first < second):
            count += 1
        first = second


    print(count)

main()