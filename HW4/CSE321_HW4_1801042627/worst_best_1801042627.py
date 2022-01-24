
from decimal import Decimal
import math
positive_infinity = Decimal('Infinity')
negative_infinity = Decimal('-Infinity')

def func(arr,start,end):

    if(end-start == 1):
        best = arr[start]
        worst = arr[start]
        return best,worst
    mid = math.floor((end+start) / 2)
 
    leftBest,leftWorst = func(arr,start,mid)
    rightBest,rightWorst = func(arr,mid,end) 
    best = leftBest
    if(rightBest>leftBest):
        best = rightBest
    worst = leftWorst
    if(rightWorst < leftWorst):
        worst = rightWorst
    return best,worst
def main():

    arr = [5,1,2,4,4,11,3,12,32,13]
    best,worst = func(arr,0,len(arr))
    print("Given array: ",end = "")
    print(arr)
    print("best:",end=" ")
    print(best)
    print("worst:",end=" ")
    print(worst)
if __name__ == "__main__":
    main()