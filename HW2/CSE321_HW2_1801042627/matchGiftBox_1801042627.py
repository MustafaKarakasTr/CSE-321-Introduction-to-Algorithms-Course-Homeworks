
#puts the pivot value to the start of arr so that 2 array has same pivot value
def putAtTheStart(arr,pivotValue,low,high): 
    for i in range(low,high):
        if(arr[i] == pivotValue):
            arr[i],arr[low] = arr[low],arr[i]
            break


def partition (arr, low,high,pivotValueFromOtherArray):
    left = low
    right = high-1
    while(left < right):
        while(left < high and arr[left] <= pivotValueFromOtherArray ):
            left = left + 1
        while(right>low and arr[right] >pivotValueFromOtherArray):
            right = right - 1
        if(left < right) :
            arr[left],arr[right] = arr[right],arr[left]
    arr[low] = arr[right]
    arr[right] = pivotValueFromOtherArray
    return right


def matchGiftBox(boxes,gifts,low,high):
    if(low>=high or low < 0 or high > len(boxes)):
        return
    putAtTheStart(gifts,boxes[low],low,high) 
    index = partition (gifts, low,high,boxes[low])
    partition(boxes, low,high,gifts[index])    
    matchGiftBox(boxes,gifts,low,index)
    matchGiftBox(boxes,gifts,index+1,high)

#test

gifts = [2,1,4,5,3]
boxes = [3,1,5,2,4]
print("Before matching boxes with gifts")

print("boxes:")
print(boxes)

print("gifts:")
print(gifts)

matchGiftBox(boxes,gifts,0,len(boxes))
print("After matching boxes with gifts")

print("boxes:")
print(boxes)

print("gifts:")
print(gifts)

