def insert_sort(arr, lo, n):
    for i in range(lo + 1, n + 1):
        k = arr[i]
        j = i
        while j > lo and arr[j - 1] > k:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = k


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = j = lo
    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[hi] = arr[hi], arr[j]
    return j


def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)
        return arr


def quick_insert_sort(arr, lo, hi):
    while lo < hi:
        if hi - lo + 1 < 10:
            insert_sort(arr, lo, hi)
            break
        else:
            pivot = partition(arr, lo, hi)
            if pivot - lo < hi - pivot:
                quick_insert_sort(arr, lo, pivot - 1)
                lo = pivot + 1
            else:
                quick_insert_sort(arr, pivot + 1, hi)
                hi = pivot - 1


if __name__ == "__main__":
    b = [24, 97, 40, 67, 88, 85, 15,
         66, 53, 44, 26, 48, 16, 52,
         45, 23, 90, 18, 49, 80, 23]
    quick_insert_sort(b, 0, len(b)-1)
    print(b)
