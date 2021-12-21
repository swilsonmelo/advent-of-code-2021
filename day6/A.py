from sys import stdin

# Slow solution

def main():

    lanternFish = [int(x) for x  in stdin.readline().split(",")]

    days = 80
    
    for i in range(days):

        newLanternFish = lanternFish.copy()

        for j in range(len(lanternFish)):

            newLanternFish[j] -= 1
            if(lanternFish[j] == 0):
                newLanternFish[j] = 6
                newLanternFish += [8]

        #print(lanternFish)    
        #print(newLanternFish)
        #print()
        
        lanternFish = newLanternFish.copy()
    
    #print(lanternFish)
    print(len(lanternFish))
    
main()