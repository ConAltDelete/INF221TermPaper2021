from numba import jit

@jit(nopython=True)
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

@jit(nopython=True)
def bubble_sort(List: list):
    n = len(List)
    while n > 1:
        newn = 0
        for i in range(1,n):
            if List[i-1] > List[i]:
                swap(List,i-1,i)
                newn = i
        n = newn

if __name__ == "__main__":
    l = [1,9,5,7,2,4]
    bobble_sort(l)
    print(l)
