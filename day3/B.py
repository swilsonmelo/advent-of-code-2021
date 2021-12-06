from sys import stdin


def main():
    
    a = stdin.readline().strip()

    numbersMax = []
    numbersMin = []

    while a:
        
        numbersMax.append(a)
        numbersMin.append(a)

        a = stdin.readline().strip()

    pos = 0

    while pos < len(numbersMax[0]):

        zeroNumbers = []
        oneNumbers = []
        zeros = 0
        ones = 0

        for i in range(len(numbersMax)):

            if(numbersMax[i][pos] == "0"):
                zeros += 1
                zeroNumbers.append(numbersMax[i])
            else:
                ones += 1
                oneNumbers.append(numbersMax[i])

        if(ones >= zeros):
            numbersMax = oneNumbers
        else:
            numbersMax = zeroNumbers


        pos += 1

    pos = 0
    
    while len(numbersMin) > 1 and pos < len(numbersMin[0]) :

        zeroNumbers = []
        oneNumbers = []
        zeros = 0
        ones = 0

        for i in range(len(numbersMin)):

            if(numbersMin[i][pos] == "0"):
                zeros += 1
                zeroNumbers.append(numbersMin[i])
            else:
                ones += 1
                oneNumbers.append(numbersMin[i])

        if(ones < zeros):
            numbersMin = oneNumbers
        else:
            numbersMin = zeroNumbers

        pos += 1

    print(int(numbersMax[0],2)*int(numbersMin[0],2))

main()