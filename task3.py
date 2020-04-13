def insertionSort( theSeq ):
    n = len( theSeq )
    for i in range( 1, n ) :
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1] :
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
            theSeq[pos] = value

x = [1,4,3,2]
insertionSort(x)
print(x)