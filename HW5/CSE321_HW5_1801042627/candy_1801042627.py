def findMaxPrice(maxProfits,i,priceOfUncutted):
    leftP = 0
    rightP = i-1
    maxProfit = priceOfUncutted
    while(leftP<=rightP):
        profit = maxProfits[leftP] + maxProfits[rightP]
        if(profit > maxProfit):
            maxProfit = profit
        rightP = rightP - 1
        leftP = leftP + 1

    return maxProfit

def func(prices,length):
    maxProfits = [0] * length # create list with length of array number of zeros
    maxProfits[0] = prices[0]
    for i in range(1,length):
        maxProfits[i] = findMaxPrice(maxProfits,i,prices[i])
    return maxProfits[length - 1]

def main():

    arr = [ 1,5,8,9,10,17,17,20]

    maxProfit = func(arr,8)
    print("Given array: ",arr,"\nMax profit: ",maxProfit)
if __name__ == "__main__":
    main()