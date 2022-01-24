stringGiven = "TXZXXJZWX"
start       = 'X'
end         = 'Z'

def count_str(str,start, end):
    numberOfStartCharacters = 0
    sum = 0
    for c in str:
        if(c == start):
            numberOfStartCharacters+=1
        elif(c == end):
            sum += numberOfStartCharacters
    return sum

if __name__ == "__main__":
    val = count_str(stringGiven,start,end)
    print(f'Result is : {val}')
