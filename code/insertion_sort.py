# -*- coding: utf-8 -*-

def insertion_sort(A):
    """
    Sorts A by the insertion sort algorithm.
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

a = [5, 1, 3, 4, 2]
insertion_sort(a)
print(a)
