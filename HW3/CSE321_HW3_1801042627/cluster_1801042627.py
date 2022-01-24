profits = [3,-5,2,11,-8,9,-5]

def mostProfitRegion(profits):
    size = len(profits)
    maxSum = 0
    start = 0
    end = 0
                
    for i in range(0,size):
        for j in range(i,size):
            sum = 0
            for k in range(i,j+1):
                sum += profits[k]
            if(sum > maxSum):
                maxSum = sum
                start = i
                end = k
    return start,end
    
if __name__ == "__main__":
    mostProfitCluster = mostProfitRegion(profits)
    print("The most profitable cluster is : ")
    for i in range(mostProfitCluster[0],mostProfitCluster[1]+1):
        print(profits[i])
