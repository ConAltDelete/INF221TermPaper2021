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
....sdaa----
"""

import time
import timeit
import random
import sys
import numpy as np
import threading
from multiprocessing import Pool

#======getting the algoritems===============
from bubble_sort        import *
from insertion_sort     import *
from mergesort_insert   import *
from mergesort          import *
from numpy_sort         import *
from python_sort        import *
from quicksort_insert   import *
from quicksort          import *
from quicksort_med3     import *
from quicksortIterative import *
from cyclesort          import *
#===========================================

from variabler import * # contains configurations

#!========DANGER, increasing depth==========!
sys.setrecursionlimit(2000)
#!==========================================!

#
# The configuration file contains:
#      - rounds: number of sizes
#      - iterations: how many times to run each test.
#

func_dir = {
    "bubble_sort"        : bubble_sort,
    "insertion_sort"     : insertion_sort,
    "mergesort_insert"   : mergesort_insert,
    "mergesort"          : mergesort,
    "numpy_sort"         : numpy_sort,
    "python_sort"        : python_sort ,
    "quicksort_insert"   : quicksort_insert,
    "quicksort"          : quicksort,
    "quicksort_med3"     : quicksort_med3,
    "quicksortIterative" : quicksortIterative,
    "cyclesort"          : cyclesort
        }

def test_func_lambda():
    pass
    

def time_test(function,func_str, parameter: list[int], n = 1000000, Apars = None, irounds = 0) -> float:
    """
    Returns the time to execute a function "function" with the parameter "parameter".
    input: a function, and a list to use in the function.
    output, float: the time taken.
    """
    global test_func_lambda
    #global log_file
    

    if parameter != "random":
        copy_param = np.array(parameter)
    else:
        copy_param = np.random.randint(0,2**Apars,size=2**Apars)

    def test_func_lambda():
        function(copy_param)

    try:
        t = timeit.timeit("test_func_lambda()", globals=globals(),number=1)
        #d1 = time.time()
        #function(copy_param)
        #d2 = time.time()
    except RecursionError:
        print("\t\t\t\tFAILED! (Due to recursion) ")
        #log_file.write("{}|{}: Recurrtion error\n".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func_str))
        return None, None, None, None
    except Exception as err:
        print("\t\t\t\tFAILED! ({})".format(err))
        #log_file.write("{}|{}: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func_str,err))
        return None, None, None, None

    avg = t
    variance = 0
    minimum = avg
    maximum = avg
    
    pre_pros = 0

    for k in range(2,n+1):
        if parameter != "random":
            copy_param = np.array(parameter)
        else:
            copy_param = np.random.randint(0,2**Apars,size=2**Apars)

        def test_func_lambda():
            function(copy_param)
        
        if round(100*k/n) != pre_pros:
            pre_pros = round(100*k/n)
            print("{} -> {}: {}% done with round {} of {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),function,pre_pros,irounds,rounds))

        #d1 = time.time()
        #function(copy_param)
        #d2 = time.time()

        
        t = timeit.timeit("test_func_lambda()", globals=globals(),number = 1) 

        avg_pre = avg

        avg += (t - avg)/k

        variance += ((t-avg_pre)*(t-avg) - variance)/k

        if t > maximum:
            maximum = t
        elif t < minimum:
            minimum = t
    print("{} -> Done:{}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),function))
    return avg, variance, minimum, maximum

def sec2hms(sec):
    hours = sec // (60*60)
    sec %= (60*60)
    minut = sec // 60
    sec %= 60
    return "%02i:%02i:%02i" % (hours,minut,sec)

def write_time(file_name: str):
    """
    runs appropriate tests and makes csv files.
    """
    #global log_file

    file_output = open("./data/csv_files/"+ file_name + ".csv","w+")
    
    file_output.write("lg2 n,{},{},{},{},{},{},{},{},{},{},{},{}\n".format("sorted","sorted variance","reversed","reversed variance","random","random variance","min_sort","min_rev","min_rand","max_sort","max_rev","max_rand"))


    #=================Makes the function to be tested===========================
    
    func = func_dir[file_name]
    #===========================================================================

    print("Performing tests on {}".format(func))
    for i in range(rounds+1):
        print("test",i,"of", rounds,":",func)

        l1 = np.arange(0,2**i)
        l2 = np.arange(2**i,0,-1)
        
        print("{} -> sorted test: {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func))
        test1, test1_vari, test1_min, test1_max = time_test(func,file_name, l1, n = iterations,irounds = i)
        print("{} -> Reversed test: {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func))
        test2, test2_vari, test2_min, test2_max = time_test(func,file_name, l2, n = iterations,irounds = i)
        print("{} -> random test: {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func))
        test3, test3_vari, test3_min, test3_max = time_test(func,file_name, "random", n = iterations, Apars = i, irounds = i)

        file_output.write("{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(i,test1,test1_vari,test2,test2_vari,test3,test3_vari,test1_min,test2_min,test3_min,test1_max,test2_max,test3_max))


    file_output.close()

    print("{} -> Tests done: {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()),func))


if __name__ == "__main__":
    test = sys.argv[1:]

    #log_file = open("./tests_log.txt","w")
    
    if len(test) == 0:
        test = list(func_dir.keys())
    
    elif any(i not in func_dir.keys() for i in test):
        print("{} are not valid arguments.".format([i for i in test if i not in func_dir.keys()]))
        print("Valid arguments are:")
        for valid_arg in func_dir.keys():
            print("\t -", valid_arg)
        exit(1)

    print("We are going to test:")
    for t in test:
        print("\t- {}".format(t))
    print("Every algorithm will run",rounds,"rounds each.")
    #print("beginning tests:")
    #for test_name in enumerate(test):
    #    print("\ttesting ",test_name[1],":")
    #    write_time(test_name[1])
    #    print("\tDone testing ", test_name[1])
    #    print("\tRemaning time for testing:",sec2hms( int( (time.time() - base_time_algo)*(len(test)-test_name[0]-1)/(test_name[0]+1) ) ))

    with Pool(min(8,len(test))) as p:
        p.map(write_time, test)
    print("{} -> All tests done".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
