from sys import stdin



def validateAdjacentPoits(i, j, matrix):

    count = 0    

    for k in range(i-1, i + 2):
        for l in range( j - 1, j + 2):
            #print(i, j, k, l)
            if(matrix[i][j] < matrix[k][l]):
                count += 1

    if(count == 8):
        return True
    
    return False

    
    

def main():

    matrix = []    

    input = list(stdin.readline().strip())
    rowSize = len(input) + 2
    matrix.append([float('inf')] * rowSize)

    while input:
        matrix.append([float('inf')] + [int(x) for x in input] + [float('inf')])
        input = list(stdin.readline().strip())

    matrix.append([float('inf')] * rowSize)

    columSize = len(matrix)

    print(rowSize, columSize)

    riskLevelsSum = 0

    for i in range(1, columSize - 1):
        for j in range(1, rowSize - 1):
            if(validateAdjacentPoits(i, j , matrix)): 
                #print(i,j)           
                riskLevelsSum += matrix[i][j] + 1
    print(riskLevelsSum)            
main()