def partision(A, p, r):
    pid = med3(A, p, int((p+r)/2), r)
    x = A[pid]
    A[pid], A[r] = A[r], A[pid]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quicksort_med3(A: list, p=None, r=None):
    if p is None:
        p = 0
    if r is None:
        r = len(A)-1
    if p < r:
        q = partision(A, p, r)
        quicksort_med3(A, p, q-1)
        quicksort_med3(A, q+1, r)


def med3(A, p, m, r):
    lo, mid, hi = A[p], A[m], A[r]
    swap = 0
    if lo > hi:
        hi, lo = lo, hi
        swap += 1
    if mid < lo:
        if swap == 1:
            return p
        else:
            return r
    elif mid > hi:
        if swap == 1:
            return r
        else:
            return p
    else:
        return m


if __name__ == "__main__":
    L = [5, 4, 1, 2, 3]
    quicksort(L,0,len(L)-1)
    print(L)
