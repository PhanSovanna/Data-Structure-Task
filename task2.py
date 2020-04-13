def selectionSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ):
        smallNdx = i
        for j in range( i + 1, n ):
            if theSeq[j] < theSeq[smallNdx] :
                smallNdx = j
        if smallNdx != i :
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

x = [1,4,3,2]
selectionSort(x)
print(x)