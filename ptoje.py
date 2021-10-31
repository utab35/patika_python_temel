 Working recursive implementation
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,[[[3,2], [3,4, 3]]]]
#
def flatten(l):
    L = []
    for elem in l:
        if type(elem) == list:
            L.extend(flatten(elem))
        else:
            L.append(elem)    
    return L
flatten(a)

def reverse_list(l):
    # base case    
    l.reverse()
    for e in l:
        if isinstance(e, list):
            e.reverse()  
    return l
L = [[1, 2], [3, 4], [5, 6, 7]]
reverse_list(L)
