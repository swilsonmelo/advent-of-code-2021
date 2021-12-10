from sys import stdin

matrix = []


for i in range(1000):
    matrix.append([0] * 1000)

def writeSegment(segment):
    global matrix

    firstPoint = segment[0]

    secondPoint = segment[1]
    
    horizontal = False
    vertical = False
   
    if(firstPoint[1] == secondPoint[1]):

        horizontal = True
        size = abs(secondPoint[0] - firstPoint[0])

    elif(firstPoint[0] == secondPoint[0]):

        vertical = True
        size = abs(secondPoint[1] - firstPoint[1])

    elif( abs(firstPoint[0] - secondPoint[0]) == abs(firstPoint[1] - secondPoint[1]) ):

        size = abs(firstPoint[0] - secondPoint[0])
        derecha = secondPoint[0]  - firstPoint[0]
        arriba = secondPoint[1] - firstPoint[1]
        
        #print(firstPoint, secondPoint)
        #print(size, derecha, arriba)

        for i in range(size + 1):

            x = firstPoint[0]
            y = firstPoint[1]

            if(derecha > 0):
                x += i
            else:
                x -= i

            if(arriba > 0):
                y += i
            else:
                y -= i

            #print("Y:", y, "X: ", x)

            matrix[y][x] += 1
                          
            

        #for i in matrix:
        #    print(i)

    

    if(horizontal or vertical):
    
        for i in range(size + 1):
            if(horizontal):
                matrix[firstPoint[1]][ firstPoint[0] + i] += 1                

            elif(vertical):
                matrix[firstPoint[1] + i][firstPoint[0]] += 1
            
def countNumbers():

    count = 0

    for i in matrix:
        for j in i:
            if(j >= 2):
                count += 1
    
    return count



def main():

    segment = stdin.readline().strip()

    while segment:

        segment = segment.split("->")            
        segment = "".join(segment)
        segment = segment.split()            
        segment = [ x.split(",") for x in segment]

        segment[0] = [int(x) for x in segment[0]]
        segment[1] = [int(x) for x in segment[1]]
        
        segment.sort()        

        writeSegment(segment)
        

        segment = stdin.readline().strip()
    
    print(countNumbers())

    #for i in matrix:
    #    print(i)

main()