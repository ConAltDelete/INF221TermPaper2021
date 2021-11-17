from numba import jit

#@jit(nopython=True)
def insert_sort(arr, lo, n):
    for i in range(lo + 1, n + 1):
        k = arr[i]
        j = i
        while j > lo and arr[j - 1] > k:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = k


#@jit(nopython=True)
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = j = lo
    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[hi] = arr[hi], arr[j]
    return j

#@jit(nopython=True)
def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)
        return arr

#@jit(nopython=True)
def quicksort_insert(arr, lo=-1, hi=-1):
    if lo < 0:
        lo = 0
    if hi < 0:
        hi = len(arr) - 1
    while lo < hi:
        if hi - lo + 1 < 10:
            insert_sort(arr, lo, hi)
            break
        else:
            pivot = partition(arr, lo, hi)
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
