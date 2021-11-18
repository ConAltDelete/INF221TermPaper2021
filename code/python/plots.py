# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:48:38 2021

@author: Sindre
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder = "../../data/csv_files/"

data = [pd.read_csv(folder+"bobble_sort.csv"),
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
    xpoints = data[0]["lg2 n"].values
    
    figur = plt.figure()
    akser = figur.add_subplot()
    
    if list_order == "sorted" or list_order == "reversed" or list_order == "random":
        for n in enumerate(data):
            akser.plot(xpoints, n[1][list_order].values, label=data_labels[n[0]])
            list_order_label = list_order
    else:
        if list_order == "best_case":
            orders = get_best_case(data)
            list_order_label = "best case"
        elif list_order == "worst_case":
            orders = get_worst_case(data)
            list_order_label = "worst case"
        for n in enumerate(data):
            order = orders[n[0]]
            akser.plot(xpoints, n[1][order].values, label=data_labels[n[0]])
        
    
    akser.set_yscale("log")
    akser.set_xlabel("List size (n)")
    akser.set_ylabel("Time (s)")
    akser.set_title("Time usage for sorting algorithms on a list in "+list_order_label+" order")
    akser.legend()
    
    plt.show()


def get_best_case(data):
    best_cases = []
    for n in enumerate(data):
        algo_orders = {"sorted": n[1]["sorted"][8], "reversed": n[1]["reversed"][8], "random": n[1]["random"][8]}
        best_cases.append(max(algo_orders, key=algo_orders.get))
    return best_cases


def get_worst_case(data):
    worst_cases = []
    for n in enumerate(data):
        algo_orders = {"sorted": n[1]["sorted"][8], "reversed": n[1]["reversed"][8], "random": n[1]["random"][8]}
        worst_cases.append(min(algo_orders, key=algo_orders.get))
    return worst_cases


if __name__ == "__main__":
    plot_time_datasize(data, data_labels, "sorted")
    plot_time_datasize(data, data_labels, "reversed")
    plot_time_datasize(data, data_labels, "random")
    plot_time_datasize(data, data_labels, "best_case")
    plot_time_datasize(data, data_labels, "worst_case")
    
