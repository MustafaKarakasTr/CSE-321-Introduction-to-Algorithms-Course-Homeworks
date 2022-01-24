def func(arr):
    maxProfit = [0] * len(arr) # create list with length of array number of zeros
    maxProfit[0] = arr[0]
    maxFound = maxProfit[0]
    for i in range (1,len(maxProfit)):
        maxProfit[i] = max(arr[i],maxProfit[i-1] + arr[i])
        if(maxProfit[i] > maxFound):
            maxFound = maxProfit[i] 
    return maxFound

def main():

    arr = [ 3,-5,2,11,-8,9,-5]
    maxProfit = func(arr)
    print("Given array: ",arr,"\nMax profit: ",maxProfit)
if __name__ == "__main__":
    main()