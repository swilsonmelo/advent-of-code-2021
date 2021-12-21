from sys import stdin

# Fast Solution

def main():
    
    lanternFish = [int(x) for x  in stdin.readline().split(",")]

    count = [0] * 10

    days = 256

    for i in lanternFish:
        count[i] += 1

    for i in range(days-1):

        for j in range(1, 10):

            count[j - 1] += count[j]
            count[j] = 0

        count[9] += count[0]
        count[7] += count[0]
        count[0] = 0

        #print(count)


    print(sum(count))

main()