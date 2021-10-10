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

This file will take a argument (or a list of arguments, still considering it...) and run the corresponding test. It should produse a csv files in a folder containing relevant data.
"""

import time
import random
import sys

#======getting the algoritems===============
from bobble_sort      import *
from insertion_sort   import *
from mergesort_insert import *
from mergesort        import *
from numpy_sort       import *
from python_sort      import *
from quicksort_insert import *
from quicksort        import *
#===========================================

from variabels import * # contains configurations

#
# The configuration file contains:
#      - rounds: number of sizes
#      - iterations: how many times to run each test.
#

func_dir = {
#    "bobble_sort"      : bobble_sort,
#    "insertion_sort"   : insertion_sort,
#    "mergesort_insert" : mergesort_insert,
#    "mergesort"        : mergesort,
    "numpy_sort"       : numpy_sort,
    "python_sort"      : python_sort #,
#    "quicksort_insert" : quicksort_insert,
#    "quicksort"        : quicksort
        }

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
        print("\t\t\t\t{}%".format(round(100*k/n)),end="\r")
        d1 = time.time()
        function(parameter)
        d2 = time.time()
        
        t = d2 - d1 

        avg += (t - avg)/(k)

        if t > maximum:
            maximum = t
        elif t < minimum:
            minimum = t
    print("\t\t\t\tDone")
    return avg, minimum, maximum

def write_time(file_name: str):
    """
    runs appropriate tests and makes csv files.
    """
    file_output = open("./code/results/"+ file_name + ".csv","w")
    
    file_output.write("lg2 n,{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8}".format("sorted","reversed","random","min_sort","min_rev","min_rand","max_sort","max_rev","max_rand"))


    #=================Makes the function to be tested===========================
    
    func = func_dir[file_name]
    #===========================================================================

    print("\tPerforming tests...")

    for i in range(rounds):
        print("\t\ttest ",i," of ", rounds)

        # want power of 2 so we get good data. probably should test odd lenght data.
        #TODO: add another test for odd length data. Should there be 3 more just for odd?
        l1 = list_sorted(2**i)
        l2 = list_reversed(2**i)
        l3 = list_random(2**i)
        
        print("\t\t\tsorted test:")
        test1, test1_min, test1_max = time_test(func, l1, iterations)
        print("\t\t\tReversed test:")
        test2, test2_min, test2_max = time_test(func, l2, iterations)
        print("\t\t\trandom test:")
        test3, test3_min, test3_max = time_test(func, l3, iterations)

        file_output.write("{:<4},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8},{:<8}".format(i,test1,test2,test3,test1_min,test2_min,test3_min,test1_max,test2_max,test3_max))

        print("\r\t\t\tNot Done\x1b[1A\x1b[1A\r\t\t\tNot Done\x1b[1A\x1b[1A\r\t\t\tNot Done\x1b[1A\x1b[1A\r") # resets printed text

    file_output.close()

    print("\t\tTests done.")


if __name__ == "__main__":
    test = sys.argv[1:]

    print("beginning tests:")

    for test_name in test:
        print("\ttesting ",test_name,":")
        write_time(test_name)
        print("\tDone testing ", test_name)

    print("All test done")
