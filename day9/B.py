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


def chekBasins(i, j, matrix):

    count = 0    

    matrix[i][j] = -1

    if(matrix[i-1][j] >= 0 and matrix[i-1][j] < 9):
        count += 1 + chekBasins(i-1, j, matrix)
    
    if(matrix[i][j-1] >= 0 and matrix[i][j-1] < 9):
        count += 1 + chekBasins(i, j-1, matrix)
    
    if(matrix[i+1][j] >= 0 and matrix[i+1][j] < 9):
        count += 1 + chekBasins(i+1, j, matrix)

    if(matrix[i][j+1] >= 0 and matrix[i][j+1] < 9):
        count += 1 + chekBasins(i, j+1, matrix)

    return count


    

def main():

    matrix = []    

    input = list(stdin.readline().strip())
    rowSize = len(input) + 2
    matrix.append([9] * rowSize)

    while input:
        matrix.append([9] + [int(x) for x in input] + [9])
        input = list(stdin.readline().strip())

    matrix.append([9] * rowSize)

    columSize = len(matrix)

    #print(rowSize, columSize)

    lowPoints = []

    for i in range(1, columSize - 1):
        for j in range(1, rowSize - 1):
            if(validateAdjacentPoits(i, j , matrix)): 
                lowPoints.append([i,j])  

    higherBasins = [float('-inf'), float('-inf'), float('-inf')]

    for i in lowPoints:

        basinSize = 1 + chekBasins(i[0], i[1] , matrix)
        
        minBasinSize = min(higherBasins)

        if(basinSize > minBasinSize):
            for j in range(3):
                if( minBasinSize == higherBasins[j]):
                    higherBasins[j] = basinSize
                    break

    result = higherBasins[0] * higherBasins[1] * higherBasins[2]
            
    print(result)            

main()