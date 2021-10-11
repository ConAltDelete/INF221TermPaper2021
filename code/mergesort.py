# -*- coding: utf-8 -*-
import math


def merge(A, p, q, r):
    """
    Sorts A by the merge sort algorithm.
    Uses 1-based indexing.
    This Python implementation is designed to be as close to the pseudocode as possible. It is not elegant Python code.
    :param A: List of numbers to be sorted.
    :param p: The index of the first element in the part to be sorted.
    :param q: Middlepoint in the part to be sorted.
    :param r: The index of the last element in the part to be sorted.
    """
    n1 = q - p + 1
    n2 = r - q
    
    L = [0] * n1
    R = [0] * n2
    
    for i in list(range(n1)):
        L[i] = A[p + i - 1]
    
    for j in list(range(n2)):
        R[j] = A[q + j]
    
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 1 - 1 # Subtract 1 to adjust to Python indexing
    j = 1 - 1 # Subtract 1 to adjust to Python indexing
    
    for k in list(range(p - 1, r)): # Subtract 1 from q to adjust to Python range object
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def mergesort(A, p, r):
    """
    Halves the list recursively and calls the merge() function
    :param A: List of numbers to be sorted.
    :param p: The index of the first element in the part to be sorted.
    :param r: The index of the last element in the part to be sorted.
    """
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
