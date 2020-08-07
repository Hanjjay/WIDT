def findm(a):
    n=len(a)
    min_idx = 0
    for i in range(1,n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
#최소갑의 위치를 알려주는 


def sel_sort(a):
    result  = [ ]
    while a:
        min_idx = findm(a)
        value= a.pop(min_idx)
        result.append(value)
    return result

d = [2,4,5,1,3]

print(sel_sort(d))
