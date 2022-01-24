def greedy(prices,weights,maxWeight):


    return greedy_helper(prices,weights,maxWeight,0)
def greedy_helper(prices,weights,maxWeight,currentProfit):

    
    #if(maxWeight )
    maxPriceDense = prices[0] / weights[0]
    index = 0
    for i in range(1,len(prices)):
        curDense = prices[i] / weights[i]
        if(curDense > maxPriceDense):
            index = i
            maxPriceDense = curDense
    if(maxPriceDense < 0 ):
        return currentProfit
    if(maxWeight <= weights[index]):
        return currentProfit + maxWeight * maxPriceDense
    #elif(maxWeight > weights[index]):
    else:
        currentWeight = weights[index]
        weights[index] = -1
        maxProfit = greedy_helper(prices,weights,maxWeight-currentWeight,currentProfit+prices[index])
        weights[index] = currentWeight
        return maxProfit
    
#priceDense = prices[0] / weights[0]
def main():

    prices = [ 10,10,6,4,15,3,8,12,200]
    weights =[ 5 ,10,3,8,10, 1,4, 4,15]
    maxWeight = 30
    maxProfit = greedy(prices,weights,maxWeight)
    print("Prices: ",prices,"\nWeights ",weights,"\nMax profit: ",maxProfit)

if __name__ == "__main__":
    main()