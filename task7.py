def linearSearch(theValues, target ) :
    n = len(theValues)
    for i in range(n) :
        if theValues[i] == target:
            return True
    return False


print(linearSearch([3,4,5,6],3))
print(linearSearch([3,4,5,6],2))
