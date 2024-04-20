import random
def quickRanSort(A, p:int, r:int):
    if p < r:
        q=partition(A,p,r)
        quickRanSort(A,p,q-1)
        quickRanSort(A,q+1,r)

def partition(A,p:int,r:int) -> int:
    idx = random.randint(p,r)
    x=A[idx]
    i=p-1
    for j in range(p,r):
        if A[j]<x:
            i+=1
            A[i],A[j] = A[j], A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
