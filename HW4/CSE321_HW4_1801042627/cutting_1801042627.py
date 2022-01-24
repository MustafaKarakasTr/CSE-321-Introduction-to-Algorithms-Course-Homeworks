import math
def func(x):
    #print(x)
    if(x == 1):
        return 0
    if(x % 2 == 0):
        return (func(x/2)+1)   
    biggerHalf = math.ceil(x / 2) 

    return (func(biggerHalf) + 1) 
    #smallerHalf = math.floor(x / 2)


def main():

    for i in range (1,20):
        print("for ",i,"m rope, needed cut: ",end = "")
        print(func(i))
if __name__ == "__main__":
    main()