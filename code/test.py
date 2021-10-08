"""
We will be using a exponatial test enviroment where we go for 

$$
size(n_i) = 2^i
$$

With 20 datapoints. This will be plottet on a logaritmic scale for readebility. 

Further on the agenda will we be using the following inputs:
    - sorted
    - reversed
    - random

every test combiantion will be ran $10^6$ times.
"""

import time
import random
import sys


def list_sorted(n: int) -> list[int]:
    """
    Returns a sorted list with size n.
    input, int: number of elements
    output, list[int]: a sorted list
    """
    return [i for i in range(n)]

def list_reversed(n: int) -> list[int]:
    """
    Returns a reversed sorted list with size n.
    input, int: number of elements
    output, list[int]: a reversed sorted list
    """
    return [i for i in range(n-1,-1,-1)]

def list_random(n: int) -> list[int]:
    """
    Returns a random list with size n.
    input, int: number of elements
    output, list[int]: a sorted list
    """
    return [random.randint(0,n) for _ in range(n)]

def time_test(function, parameter: list[int], n = 1000000) -> float:
    """
    Returns the time to execute a function "function" with the parameter "parameter".
    input: a function, and a list to use in the function.
    output, float: the time taken.
    """
    d1 = time.time()
    function(parameter)
    d2 = time.time()

    avg = d2-d1
    minimum = avg
    maximum = avg

    for k in range(2,n+1):
        print("{}%".format(round(100*k/n),end="\r")
        d1 = time.time()
        function(parameter)
        d2 = time.time()
        
        t = d2 - d1 

        avg += (t - avg)/(k)

        if t > maximum:
            maximum = t
        elif t < minimum:
            minimum = t

    return avg, minimum, maximum

def write_time():
    file_name = sys.argv()[1]

    file_output = open(file_name + ".csv","w")
    
    file_output.write("lg2 n,{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8}".format("sorted","reversed","random","min_sort","min_rev","min_rand","max_sort","max_rev","max_rand"))
    eval("from {} import *".format(file_name))
    
    eval("import {}".format(file_name))

    func = getattr(file_name, file_name)

    print("Performing tests...")

    for i in range(20):
        print("test ",i)
        l1 = list_sorted(2**i)
        l2 = list_reversed(2**i)
        l3 = list_random(2**i)

        test1, test1_min, test1_max = time_test(func, l1)
        test2, test2_min, test2_max = time_test(func, l2)
        test3, test3_min, test3_max = time_test(func, l3)
        
        file_output.write("{:<4},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8}".format(i,round(test1),round(test2),round(test3),round(test1_min),round(test2_min),round(test3_min),round(test1_max),round(test2_max),round(test3_max)))

    file_output.close()

    print("Tests done.")


if __name__ == "__main__":
    write_time()
