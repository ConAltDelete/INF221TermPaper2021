"""
This file does the same thing as "test.py" however this file will run for `run_time` hours. This is to make sure that we can get predictible runtime on the code. Although we will get inconsistent number of data-points.
"""
import time
import random
import sys
import numpy as np

#======getting the algoritems===============
from bobble_sort      import *
from insertion_sort   import *
from mergesort_insert import *
from mergesort        import *
from numpy_sort       import *
from python_sort      import *
from quicksort_insert import *
from quicksort        import *
from quicksort_med3   import *
#===========================================

from variabler import * # contains configurations

#!========DANGER, increasing depth==========!
sys.setrecursionlimit(2000)
#!==========================================!

#
# The configuration file contains:
#      - rounds     : number of sizes
#      - iterations : how many times to run each test.
#      - run_time   : how many hours it shall run
#

func_dir = {
    "bobble_sort"      : bobble_sort,
    "insertion_sort"   : insertion_sort,
    "mergesort_insert" : mergesort_insert,
    "mergesort"        : mergesort,
    "numpy_sort"       : numpy_sort,
    "python_sort"      : python_sort ,
    "quicksort_insert" : quicksort_insert,
    "quicksort"        : quicksort,
    "quicksort_med3"   : quicksort_med3
        }

base_time = 0
number_of_funcs = len(func_dir)
timeout = False

def time_test(function, parameter: list[int], n = 10000, Apars = None) -> float:
    """
    Returns the time to execute a function "function" with the parameter "parameter".
    input: a function, and a list to use in the function.
    output, float: the time taken.
    """
    
    global timeout

    if parameter != "random":
        copy_param = np.array(parameter)
    else:
        copy_param = np.random.randint(0,2**Apars,size=2**Apars)

    try:
        d1 = time.time()
        function(copy_param)
        d2 = time.time()
    except RecursionError:
        print("\t\t\t\tFAILED! (Due to recursion) ")
        return None, None, None, None
    except Exception as err:
        print("\t\t\t\tFAILED! ({})".format(err))
        return None, None, None, None

    avg = d2-d1
    variance = 0
    minimum = avg
    maximum = avg
    
    limit = (run_time*60*60)/number_of_funcs
    
    for k in range(2,n+1):
        if ((time.time()-base_time) > limit) or timeout:
            timeout = True
            print("\t\t\t\tTIMEOUT!")
            break
        if parameter != "random":
            copy_param = np.array(parameter)
        else:
            copy_param = np.random.randint(0,2**Apars,size=2**Apars)

        print("\t\t\t\t{}%".format(round(100*k/n)),end="\r")

        d1 = time.time()
        function(copy_param)
        d2 = time.time()
        
        t = d2 - d1 

        avg_pre = avg

        avg += (t - avg)/k

        variance += ((t-avg_pre)*(t-avg) - variance)/k

        if t > maximum:
            maximum = t
        elif t < minimum:
            minimum = t
    print("\t\t\t\tDone")
    return avg, variance, minimum, maximum

def write_time(file_name: str):
    """
    runs appropriate tests and makes csv files.
    """
    
    global timeout

    file_output = open("./data/csv_files/"+ file_name + ".csv","w+")
    
    file_output.write("lg2 n,{},{},{},{},{},{},{},{},{},{},{},{}\n".format("sorted","sorted variance","reversed","reversed variance","random","random variance","min_sort","min_rev","min_rand","max_sort","max_rev","max_rand"))


    #=================Makes the function to be tested===========================
    
    func = func_dir[file_name]
    #===========================================================================

    print("\tPerforming tests...")

    i = 0
    limit = run_time*60*60/number_of_funcs

    while (time.time() - base_time) < limit:

        print("\t\ttest ",i," of infinity:")

        # want power of 2 so we get good data. probably should test odd lenght data.
        l1 = np.arange(0,2**i)
        l2 = np.arange(2**i,0,-1)
        
        
        print("\t\t\tsorted test:")
        test1, test1_vari, test1_min, test1_max = time_test(func, l1, n = iterations)
        print("\t\t\tReversed test:")
        test2, test2_vari, test2_min, test2_max = time_test(func, l2, n = iterations)
        print("\t\t\trandom test:")
        test3, test3_vari, test3_min, test3_max = time_test(func, "random", Apars = i, n = iterations)
        
        if not(timeout):
            file_output.write("{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(i,test1,test1_vari,test2,test2_vari,test3,test3_vari,test1_min,test2_min,test3_min,test1_max,test2_max,test3_max))
        else:
            timeout = False

        i += 1

    file_output.close()

    print("\t\tTests done.")


if __name__ == "__main__":
    test = sys.argv[1:]
    
    if len(test) == 0:
        test = list(func_dir.keys())
    
    elif any(i not in func_dir.keys() for i in test):
        print("{} are not valid arguments.".format([i for i in test if i not in func_dir.keys()]))
        print("Valid arguments are:")
        for valid_arg in func_dir.keys():
            print("\t -", valid_arg)
        exit(1)

    print("beginning tests:")

    number_of_funcs = len(test)

    for test_name in test:
        base_time = time.time()
        print("\ttesting ",test_name,":")
        write_time(test_name)
        print("\tDone testing ", test_name)

    print("All tests done")
