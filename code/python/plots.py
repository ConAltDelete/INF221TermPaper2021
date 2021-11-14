# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:48:38 2021

@author: Sindre
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder = "../../data/csv_files_roy/"

data_bubble_sort = pd.read_csv(folder+"bobble_sort.csv")
#data_cyclesort = pd.read_csv(folder+"cyclesort.csv")
data_insertion_sort = pd.read_csv(folder+"insertion_sort.csv")
data_mergesort = pd.read_csv(folder+"mergesort.csv")
data_mergesort_insert = pd.read_csv(folder+"mergesort_insert.csv")
data_numpy_sort = pd.read_csv(folder+"numpy_sort.csv")
data_python_sort = pd.read_csv(folder+"python_sort.csv")
#data_quicksort = pd.read_csv(folder+"quicksort.csv")
data_quicksort_insert = pd.read_csv(folder+"quicksort_insert.csv")
#data_quicksort_med3 = pd.read_csv(folder+"quicksort_med3.csv")
data_quicksortiterative = pd.read_csv(folder+"quicksortiterative.csv")


def plot_time_datasize(list_order):
    xpoints = data_bubble_sort["lg2 n"].values
    
    figur = plt.figure()
    akser = figur.add_subplot()
    
    akser.plot(xpoints, data_bubble_sort[list_order].values, label="Bubble sort")
    akser.plot(xpoints, data_insertion_sort[list_order].values, label="Insertion sort")
    akser.plot(xpoints, data_mergesort[list_order].values, label="Mergesort")
    akser.plot(xpoints, data_mergesort_insert[list_order].values, label="Mergesort insert")
    akser.plot(xpoints, data_numpy_sort[list_order].values, label="Numpy sort")
    akser.plot(xpoints, data_python_sort[list_order].values, label="Python sort")
    akser.plot(xpoints, data_quicksort_insert[list_order].values, label="Quicksort insert")
    akser.plot(xpoints, data_quicksortiterative[list_order].values, label="Quicksort iterative")
    
    akser.set_yscale("log")
    akser.set_xlabel("List size (n)")
    akser.set_ylabel("Time (s)")
    akser.set_title("Time usage for sorting algorithms on a list in "+list_order+" order")
    akser.legend()
    
    plt.show()


if __name__ == "__main__":
    plot_time_datasize("sorted")
    plot_time_datasize("reversed")
    plot_time_datasize("random")
    
