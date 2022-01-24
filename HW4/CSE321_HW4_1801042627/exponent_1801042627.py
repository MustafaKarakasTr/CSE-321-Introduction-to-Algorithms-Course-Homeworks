def bruteForceExponentiation(n, power):
    mult = 1
    for i in range (power):
        mult = mult * n
    return mult
def divideAndConquerExponentiation(n,power):
    if(power == 0):
        return 1
    if(power == 1):
        return n
    if(power % 2 == 0):
        temp = divideAndConquerExponentiation(n,power/2)
        return temp * temp
    else: # power is not even
        temp = divideAndConquerExponentiation(n,(power-1)/2)
        return temp * temp * n
def main():
    print("Enter number: ", end ="")
    n = int(input())
    print("Enter power of the number: ",end ="")
    a = int(input())
    print("Brute force answer: ",end = "")
    print(bruteForceExponentiation(n,a))

    print("Divide and conquer answer: ",end = "")
    print(divideAndConquerExponentiation(n,a))


if __name__ == "__main__":
    main()
