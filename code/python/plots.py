# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:48:38 2021

@author: Sindre
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder = "./data/csv_files_backup/"

data = [pd.read_csv(folder+"bubble_sort.csv"),
        pd.read_csv(folder+"insertion_sort.csv"),
        pd.read_csv(folder+"mergesort.csv"),
        pd.read_csv(folder+"mergesort_insert.csv"),
        pd.read_csv(folder+"numpy_sort.csv"),
        pd.read_csv(folder+"python_sort.csv"),
        pd.read_csv(folder+"quicksort_insert.csv"),
        pd.read_csv(folder+"quicksortiterative.csv")]

data_labels = ["Bubble sort", "Insertion sort", "Mergesort", "Mergesort insert",
               "Numpy sort", "Python sort", "Quicksort insert", "Quicksort iterative"]


def plot_time_datasize(data, data_labels, list_order):
    
    figur = plt.figure()
    akser = figur.add_subplot()
    
    if list_order in ["sorted","reversed","random"]:
        for n in enumerate(data):
            xpoints = n[1]["lg2 n"].values
            akser.plot(xpoints, n[1][list_order].values, label=data_labels[n[0]])
            list_order_label = list_order
    else:
        list_order_label = "best case" if list_order == "best_case" else "worst case"
        orders = get_case(data,max if list_order_label == "best case" else min)
        for n in enumerate(data):
            xpoints = n[1]["lg2 n"].values
            order = orders[n[0]]
            akser.plot(xpoints, n[1][order].values, label=data_labels[n[0]])
        
    akser.set_yscale("log")
    akser.set_xlabel("List size log2(n)")
    akser.set_ylabel("Time (s)")
    akser.set_title("Time usage for sorting algorithms on a list in "+list_order_label+" order")
    akser.legend()
    
    plt.savefig("./data/pics/"+list_order+".pdf")
    plt.clf()


def get_case(data, f):
    cases = []
    for n in data:
        algo_orders = {"sorted": list(n["sorted"]), "reversed": list(n["reversed"]), "random": list(n["random"])}
        cases.append(f(algo_orders, key=algo_orders.get))
    return cases


if __name__ == "__main__":
    labels = ["sorted","reversed","random","best_case","worst_case"]
    for l in labels:
        plot_time_datasize(data, data_labels, l)
