from numba import jit

@jit(nopython=True)
def swap(A:list, i:int, j:int):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

@jit(nopython=True)
def insert_sort(arr, lo, n):
    for i in range(lo + 1, n + 1):
        k = arr[i]
        j = i
        while j > lo and arr[j - 1] > k:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = k


@jit(nopython=True)
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = j = lo
    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[hi] = arr[hi], arr[j]
    return j


@jit(nopython=True)
def partision_mod(A:list, p:int, r:int):
    mid = (p+r)//2

    if A[mid] < A[p]:
        swap(A,mid,p)
    if A[r] < A[p]:
        swap(A,r,p)
    if A[mid] < A[r]:
        swap(A,r,mid)

    x = A[r]
    i = p
    gt = r
    lt = p
    while i <= gt:
        if A[i] == x:
            i += 1
        elif A[i] < x:
            swap(A,lt,i)
            lt += 1
            i += 1
        elif A[i] > x:
            swap(A,gt,i)
            gt -= 1
    return (gt+lt)//2

@jit(nopython=True)
def quicksort_insert(arr, lo=-2, hi=-2):
    if lo < -1:
        lo = 0
    if hi < -1:
        hi = len(arr) - 1
    while lo < hi:
        if hi - lo + 1 < 10:
            insert_sort(arr, lo, hi)
            break
        else:
            pivot = partision_mod(arr, lo, hi)
            if pivot - lo < hi - pivot:
                quicksort_insert(arr, lo, pivot - 1)
                lo = pivot + 1
            else:
                quicksort_insert(arr, pivot + 1, hi)
                hi = pivot - 1


if __name__ == "__main__":
    b = [24, 97, 40, 67, 88, 85, 15,
         66, 53, 44, 26, 48, 16, 52,
         45, 23, 90, 18, 49, 80, 23]
    quicksort_insert(b)
    print(b)
