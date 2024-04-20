
def quickEvenSort(A, p:int, r:int):
    if p < r:
        q=partition(A,p,r)
        quickEvenSort(A,p,q-1)
        quickEvenSort(A,q+1,r)

def partition(A,p:int,r:int) -> int:
    x=A[r]
    i=p-1
    sw=1
    for j in range(p,r):
        if A[j]<x or (A[j]==x and sw==1):
            i+=1
            A[i],A[j] = A[j], A[i]

        if A[j]==x:
            sw *= -1

    A[i+1],A[r] = A[r],A[i+1]
    return i+1
