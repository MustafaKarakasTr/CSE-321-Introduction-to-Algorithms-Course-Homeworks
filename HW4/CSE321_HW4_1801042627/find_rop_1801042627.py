def func(arr):
    return mergeCount(arr,0,len(arr))
def mergeCount(arr,start,end):
    lst = []
    for i in range (len(arr)):
        lst.append(arr[i])
    return mergeSort(lst)

def mergeSort(arr):
    notOrdered = 0
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        notOrderedL = mergeSort(L)

        # Sorting the second half
        notOrderedR= mergeSort(R)

        i = j = k = 0
        num = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                notOrdered = notOrdered + num
                num = 0
            else:
                num = num + 1
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            notOrdered = notOrdered+len(R)
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            
            arr[k] = R[j]
            j += 1
            k += 1
        return (notOrderedL + notOrderedR + notOrdered)
    return notOrdered

# Code to print the list


# Driver Code
if __name__ == '__main__':
    arr = [10,3,4,2,5,7,9,11]
    print("Given array is", )
    print(arr)
    answer = func(arr)
    print("Number of pairs which is not in order: ",answer)