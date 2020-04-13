def bubbleSort(_list):
    n = len(_list)
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(0, n-1):
            if _list[i] > _list[i+1]:
                did_swap = True
                _list[i+1], _list[i] = _list[i], _list[i+1]
    return _list


print(bubbleSort([10,2,3,5,3,2]))
