

def meaningfulFinder(arr,k):
    return meaningfulFinder_helper (arr,k,0)
def meaningfulFinder_helper(arr,k,start):
    min = start
    for i in range (start,len(arr)):
        if(arr[min] > arr[i]):
            min = i
    if(k > 1):
        swap(arr,min,start) # put smallest element to the leftmost position
        temp = meaningfulFinder_helper(arr,k-1,start+1)
        swap(arr,min,start) # at the end of recursion redo swap to protect order of array 
        return temp
    return arr[min]

def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
def main():

    arr = [5,14,2,41,12,43,11,3,12,32,13]

    for i in range (1,len(arr)+1):
        print("Given array: ",end="")
        print(arr)
        print("the success rate of the first meaningful ",i,". experiment:",end = " ")
        print(meaningfulFinder(arr,i))
        print("")

if __name__ == "__main__":
    main()