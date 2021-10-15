def partision(A, p, r):
    x = med3(A, p, int((p+r)/2), r)
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i], A[p] = A[p], A[i]
    return i + 1


def quicksort(A: list, p=None, r=None):
    if p is None:
        p = 0
    if r is None:
        r = len(A)-1
    if p < r:
        q = partision(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def med3(A, p, m, r):
    lo, mid, hi = A[p], A[m], A[r]
    if lo > hi:
        hi, lo = lo, hi
    if mid < lo:
        return lo
    elif mid > hi:
        return hi
    else:
        return mid


if __name__ == "__main__":
    L = [4, 5, 2, 3, 1]
    quicksort(L,0,len(L)-1)
    print(L)