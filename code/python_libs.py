import numpy as np

def python_sort(List: list) -> list:
    
    return List.sort()

def numpy_sort(List: list) -> int:

    return np.sort(List)

run = [python_sort, numpy_sort]
