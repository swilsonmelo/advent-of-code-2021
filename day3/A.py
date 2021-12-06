from sys import stdin


def main():
    
    a = stdin.readline().strip()

    zeros = []
    ones = []

    while a:
        
        for i in range(len(a)):

            if(i >= len(zeros)):
                zeros.append(0)
                ones.append(0)

            if(a[i] == "0"):
                zeros[i] += 1
            
            if(a[i] == "1"):
                ones[i] += 1

        a = stdin.readline().strip()

    gamma = ""
    epsilon = ""

    for i in range(len(zeros)):
        if(ones[i] >= zeros[i]):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma,2) * int(epsilon,2))


main()