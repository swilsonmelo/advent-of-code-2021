from sys import stdin

easyNumbers = {}
# easyNumbers[len of the number] = real number
easyNumbers[2] = 1
easyNumbers[4] = 4
easyNumbers[3] = 7
easyNumbers[7] = 8

finalOrder =[[0,1,2,4,5,6],
 [2,5],
 [0,2,3,4,6],
 [0,2,3,5,6],
 [1,2,3,5],
 [0,1,3,5,6],
 [0,1,3,4,5,6],
 [0,2,5],
 [0,1,2,3,4,5,6],
 [0,1,2,3,5,6]]

#I am not proud of this solution, but I don't want to know more about this exercise...

def getDifference(n1, n2):

    result = []

    for i in n1:
        if( not i in n2):
            result.append(i)     
    
    return result


def validateSixNineAndZero(correctOrder, numbers):

    """
    9      6      0
    bcdefg acdefg abdefg
    
    9 - 6 = b
    9 - 0 = c

    6 - 9 = a
    6 - 0 = c

    0 - 6 = b
    0 - 9 = a
    """

    six = []
    nine = []
    zero = []

    sixNineZero = []

    for i in numbers:
        if( len(i) == len(finalOrder[6]) ):
            sixNineZero.append(i)

    #print(sixNineZero)
    difference1 = getDifference(sixNineZero[0], sixNineZero[1])[0]
    #print(difference1)
    difference2 = getDifference(sixNineZero[0], sixNineZero[2])[0]
    #print(difference2)

    if( (difference1 in correctOrder[5] or difference1 in correctOrder[1]) 
        and (difference2 in correctOrder[5] or difference2 in correctOrder[1]) ):

        nine = sixNineZero[0]
         
        if(difference1 in correctOrder[5]):
            six = sixNineZero[1]
            newOrder = getDifference(correctOrder[5], difference1)
            correctOrder[5] = newOrder
            correctOrder[2] = [difference1]

        if(difference2 in correctOrder[5]):
            six = sixNineZero[2]
            newOrder = getDifference(correctOrder[5], difference2)
            correctOrder[5] = newOrder
            correctOrder[2] = [difference2]

        if(difference1 in correctOrder[1]):
            zero = sixNineZero[1]
            newOrder = getDifference(correctOrder[1], difference1)
            correctOrder[1] = newOrder
            correctOrder[3] = [difference1]

        if(difference2 in correctOrder[1]):
            zero = sixNineZero[2]
            newOrder = getDifference(correctOrder[1], difference2)
            correctOrder[1] = newOrder
            correctOrder[3] = [difference2]
    
    if( (difference1 in correctOrder[6] or difference1 in correctOrder[1]) 
        and (difference2 in correctOrder[6] or difference2 in correctOrder[1]) ):

        six = sixNineZero[0]

        if(difference1 in correctOrder[6]):
            nine = sixNineZero[1]
            newOrder = getDifference(correctOrder[6], difference1)
            correctOrder[6] = newOrder
            correctOrder[4] = [difference1]

        if(difference2 in correctOrder[6]):
            nine = sixNineZero[2]
            newOrder = getDifference(correctOrder[6], difference2)
            correctOrder[6] = newOrder
            correctOrder[4] = [difference2]
        
        if(difference1 in correctOrder[1]):
            zero = sixNineZero[1]
            newOrder = getDifference(correctOrder[1], difference1)
            correctOrder[1] = newOrder
            correctOrder[3] = [difference1]

        if(difference2 in correctOrder[1]):
            zero = sixNineZero[2]
            newOrder = getDifference(correctOrder[1], difference2)
            correctOrder[1] = newOrder
            correctOrder[3] = [difference2]

    if( (difference1 in correctOrder[5] or difference1 in correctOrder[6]) 
        and (difference2 in correctOrder[5] or difference2 in correctOrder[6]) ):

        zero = sixNineZero[0]

        if(difference1 in correctOrder[5]):
            six = sixNineZero[1]
            newOrder = getDifference(correctOrder[5], difference1)
            correctOrder[5] = newOrder
            correctOrder[2] = [difference1]

        if(difference2 in correctOrder[5]):
            six = sixNineZero[2]
            newOrder = getDifference(correctOrder[5], difference2)
            correctOrder[5] = newOrder
            correctOrder[2] = [difference2]
        
        if(difference1 in correctOrder[6]):
            nine = sixNineZero[1]
            newOrder = getDifference(correctOrder[6], difference1)
            correctOrder[6] = newOrder
            correctOrder[4] = [difference1]

        if(difference2 in correctOrder[6]):
            nine = sixNineZero[2]
            newOrder = getDifference(correctOrder[6], difference2)
            correctOrder[6] = newOrder
            correctOrder[4] = [difference2]


    #print(nine, six, zero)
    #print(sixNineZero)
    #print(correctOrder)
    return correctOrder

def organizeNumbers(correctAsignation1, numbers):

    correctOrder = []

    for i in range(7):
        correctOrder.append([])
    
    getPosition0 = getDifference(correctAsignation1[7], correctAsignation1[1])
    correctOrder[0] += getPosition0

    getPosition2And5 = getDifference(correctAsignation1[7], correctOrder[0][0])
    correctOrder[2] += getPosition2And5
    correctOrder[5] += getPosition2And5[::-1]

    getPosition1And3 = getDifference(correctAsignation1[4], correctAsignation1[1])
    correctOrder[1] += getPosition1And3
    correctOrder[3] += getPosition1And3[::-1]

    n8Minusn7 = getDifference(correctAsignation1[8], correctAsignation1[7])    
    n8Minusn4And7 = getDifference("".join(n8Minusn7), correctAsignation1[4])
    correctOrder[4] += n8Minusn4And7
    correctOrder[6] += n8Minusn4And7[::-1]

    #print(correctOrder)
    #print(correctAsignation1)

    correctOrder = validateSixNineAndZero(correctOrder, numbers)
    #print(correctOrder)
    for i in range(7):

        if(len(correctOrder[i]) < 2 ):
            correctOrder[i] += correctOrder[i]

    return correctOrder


def main():

    input = stdin.readline().strip().split("|")

    result = 0

    while input[0] != "":

        #print(input)
        #print(len(input))

        numbers = [list(x) for x in input[0].split()]
        queries = [list(x) for x in input[1].split()]

        # correctAsignation[number] = representation
        correctAsignation1 = {}
        correctAsignation2 = {}

        uniqueNumbers = []

        for i in range(len(queries)):
            representation = queries[i]
            representation.sort()
            queries[i] = "".join(representation)

        for i in range(10):

            representation = numbers[i]
            representation.sort()
            representation = "".join(representation)
            numbers[i] = representation
            
            if( len(representation) in easyNumbers ):
        
                number = easyNumbers[len(representation)]
                correctAsignation1[number] = representation
                correctAsignation2[representation] = number

        for i in queries:
            if(i in correctAsignation2):
                uniqueNumbers.append(correctAsignation2[i])

        
    
        correctOrder = organizeNumbers(correctAsignation1, numbers)
                
        #print(correctOrder)

        solutions = []
        for i in range(10):
            solutions.append([])

        for i in range(2):
            for j in range(10):

                number = []

                for k in finalOrder[j]:
                    number += correctOrder[k][i]
                number.sort()
                solutions[j] += ["".join(number)]

        #print(solutions)
        #print(queries)
            
        finalNumber = ""
        for i in queries:
            for j in range(10):
                if( i in solutions[j] ):
                    finalNumber += str(j)
        #print(finalNumber)

        result += int(finalNumber)
        
        
        input = stdin.readline().strip().split("|")
    
    print(result)

main()