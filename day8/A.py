from sys import stdin

easyNumbers = {}

# easyNumbers[len of the number] = real number
easyNumbers[2] = 1
easyNumbers[4] = 4
easyNumbers[3] = 7
easyNumbers[7] = 8

def main():

    input = stdin.readline().strip().split("|")

    result = 0

    while input[0] != "":

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
                

        #print(numbers)
        #print(queries)        
        #print(uniqueNumbers)
        #print()

        result += len(uniqueNumbers)
        input = stdin.readline().strip().split("|")
    
    print(result)
    
    

main()