from sys import stdin

def main():

    crabs = [int(x) for x in stdin.readline().strip().split(",")]
    
    avg = int(sum(crabs) / len(crabs))

    totalFuel = 0

    for i in crabs:

        difference = int(abs(i - avg))

        totalFuel += (difference * (difference + 1))/2

    print(avg)
    print(totalFuel)

main()