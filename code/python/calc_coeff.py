import coeff_estimat as ce
import math
import numpy as np

import operator as op

"""
load data -> load funcs -> estimate
"""

def logic_comp(a,b,flag, n0 = -1, strict = True):
    """
        flags(bits):
            - bit 1: less
            - bit 2: equal
            - bit 3: greater
            - bit 4: not equal

        a,b er data arrays.
    """
    if len(a) != len(b):
        raise ValueError("size of a not equal to size of b; len(a) = {}, len(b) = ".format(len(a),len(b)))
    
    data_zip = zip(a,b)

    flag_funcs = [op.lt,op.eq,op.gt,op.ne]
    if n0 >= len(a)-1:
        return False
    if strict:
        truth = all(all(f(data[0],data[1]) for k,data in enumerate(data_zip) if k>n0) for b,f in enumerate(flag_funcs) if ((flag>>b)&1)!=0)
    else:
        truth = any(all(f(data[0],data[1]) for k,data in enumerate(data_zip) if k>n0) for b,f in enumerate(flag_funcs) if ((flag>>b)&1)!=0)
    return truth

if __name__ == "__main__":
    algol_list = [
            "numpy_sort",
            "python_sort",
            "insertion_sort",
            "bubble_sort",
            "cyclesort",
            "mergesort_insert",
            "mergesort",
            "quicksort",
            "quicksort_insert",
            "quicksortIterative"
            ]
    collected_data = ce.get_data("./data/csv_files_backup/",algol_list) #TODO: Dataen's x er log2()

    for i,key in enumerate(collected_data):
        collected_data[key]["data"][i][0] = 2**collected_data[key]["data"][i][0]

    funcs = [
            lambda x: 1,
            lambda x: x,
            lambda x: x**2,
            lambda x: x*math.log2(x),
            lambda x: math.log2(x)
            ]
    algol_funcs = {
            "numpy_sort": {"random":[funcs[2]]},
            "python_sort": {"random":[funcs[3]]},
            "insertion_sort": {"random":[funcs[2]]},
            "quicksort": {"random":[funcs[2]]},
            "mergesort": {"random":[funcs[3]]},
            "cyclesort": {"random":[funcs[2]]},
            "quicksort_insert": {"random":[funcs[2]]},
            "bubble_sort": {"random":[funcs[2]]},
            "mergesort_insert": {"random":[funcs[3]]}#,
            #"quicksortIterative": {"random":[funcs[2]]}
            }

    label = "random"

    results = dict()
    
    print("\n:Calculating coeffs:\n")

    for data in collected_data.keys() & algol_funcs.keys(): 
        index_label = collected_data[data]["head"].index(label)

        data_fetch = [
                    [],
                    []
                ]
        for row in collected_data[data]["data"]:
            data_fetch[0].append(2**row[0])
            data_fetch[1].append(row[index_label])
        
        if len(data_fetch) == 0:
            continue
        print(data, end = ": ")
        print(result := abs(float(ce.mod_regrass(data_fetch,algol_funcs[data][label])[0,0])),end="-> trying estimation: ")

        results[data] = result
        
        # O-claculation

        n0 = -1
        scaler = 1

        scale_lim = 100000

        while scaler < scale_lim:
            # print(n0,scaler)
            list_a = list(map(lambda x: scaler*result*algol_funcs[data][label][0](float(x)),data_fetch[0]))
            #print(list_a,data_fetch[1])
            if logic_comp(list_a,data_fetch[1],int("100",2),n0=n0):
                break
            elif n0 >= len(data_fetch[0])/2:
                n0 = -1
                scaler += 1
            else:
                n0 += 1

        if scaler >= scale_lim:
            print("estimation Failed!")
        else:
            print("estimation succsess! coff={}, n0={}".format(scaler*result,n0))
            print("\testimated\tdata")
            for a in zip(list_a,data_fetch[1]):
                print("\t{}\t{}".format(a[0],a[1]))
