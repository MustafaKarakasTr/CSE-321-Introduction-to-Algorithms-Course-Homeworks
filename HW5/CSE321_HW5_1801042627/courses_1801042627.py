def greedyHelper(starts,ends,isCourseTakenArr):
    earlyCourseStart = starts[0]
    earlyCourseEnd = ends[0]
    lastEnd = 0
    index = 0
    numberOfCourses = 0
    isAnyCourseAvailable = True
    while(True):
        minStartFound = -1
        for i in range (len(starts)):
            if(isCourseTakenArr[i] == False and starts[i] >= lastEnd):
                minStartFound = starts[i]
                minStartFoundIndex = i
                break
        if(minStartFound == -1):
            return numberOfCourses
        numberOfFounds = 0
        for i in range ( len(starts)):
            if(isCourseTakenArr[i] == False and minStartFound >= starts[i] and lastEnd <= starts[i]):
                numberOfFounds = numberOfFounds + 1
                if(minStartFound == starts[i] and ends[i] >= ends[minStartFoundIndex] and numberOfFounds > 1):
                   print("",end="") # does nothing
                else:
                    index = i
                    minStartFound = starts[i]
        isCourseTakenArr[index] = True
        lastEnd = ends[index]
        numberOfCourses = numberOfCourses + 1 

def greedy(starts,ends):
    return greedyHelper(starts,ends,[False] * len(starts))  
#priceDense = prices[0] / weights[0]
def main():

    starts = [ 1,3,0,5,8,5]
    ends =   [2,4,2,7,9,9 ]
    maxCourses = greedy(starts,ends)
    print("Starts: ",starts,"\nEnds:   ",ends)
    print("max number of courses: ",maxCourses)

if __name__ == "__main__":
    main()