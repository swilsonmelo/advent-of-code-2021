from sys import stdin

def main():

    crabs = [int(x) for x in stdin.readline().strip().split(",")]
    
    largestNumber = max(crabs)

    totalFuel = float('inf')

    average = 0

    for i in range(largestNumber + 1):

        fuel = 0

        for j in crabs:

            difference = abs(i - j)

            delta = (difference * (difference + 1))/2

            fuel += delta

        if(fuel < totalFuel):
            totalFuel = fuel
            average = i

    print(totalFuel)
    print(average)

main()