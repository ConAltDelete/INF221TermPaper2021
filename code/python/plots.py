# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:48:38 2021

@author: Sindre
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

folder = "../../data/csv_files_roy/"
pic_folder = "../../data/pics/"

data = [pd.read_csv(folder+"bubble_sort.csv"),
        pd.read_csv(folder+"insertion_sort.csv"),
        pd.read_csv(folder+"mergesort.csv"),
        pd.read_csv(folder+"mergesort_insert.csv"),
        pd.read_csv(folder+"numpy_sort.csv"),
        pd.read_csv(folder+"python_sort.csv"),
        pd.read_csv(folder+"quicksort_insert.csv"),
        pd.read_csv(folder+"quicksort.csv")]

data_labels = ["Bubble sort", "Insertion sort", "Mergesort", "Mergesort insert",
               "Numpy sort", "Python sort", "Quicksort insert", "Quicksort iterative"]


def plot_time_datasize(data, data_labels, list_order):
    xpoints = data[0]["lg2 n"].values
    
    figur = plt.figure()
    akser = figur.add_subplot()
    
    if list_order in ["sorted","reversed","random"]:
        for n in enumerate(data):
            akser.plot(xpoints, n[1][list_order].values, label=data_labels[n[0]], marker='o', markersize=3)
            list_order_label = list_order
    elif list_order in ["worst_case","best_case"]:
        if list_order == "best_case":
            orders = get_best_or_worst_case(data, "best")
            list_order_label = "best case"
        elif list_order == "worst_case":
            orders = get_best_or_worst_case(data, "worst")
            list_order_label = "worst case"
        for n in enumerate(data):
            order = orders[n[0]]
            akser.plot(xpoints, n[1][order].values, label=data_labels[n[0]], marker='o', markersize=3)
    else:
        raise ValueError("Not valid parameter, got " + list_order)
        
    quadratic_plot(xpoints, akser)
    nlogn_plot(xpoints, akser)
    
    akser.set_yscale("log")
    akser.set_xlabel("List size (2^n)")
    akser.set_ylabel("Time (s)")
    akser.set_title("Time usage for sorting algorithms on a list in "+list_order_label+" order")
    akser.legend()
    
    plt.savefig(pic_folder+list_order+".pdf")
    plt.show()


def get_case(data, f):
    cases = []
    for n in data:
        algo_orders = {"sorted": list(n["sorted"]), "reversed": list(n["reversed"]), "random": list(n["random"])}
        cases.append(f(algo_orders, key=algo_orders.get))
    return cases


def get_best_or_worst_case(data, best_or_worst):
    """
    Returns a list of each algorithm's best or worst case input list. Either "sorted", "reversed" or "random".
    """
    best_or_worst_cases = []
    for n in enumerate(data):
        algo_orders = {"sorted": n[1]["sorted"][8], "reversed": n[1]["reversed"][8], "random": n[1]["random"][8]}
        if best_or_worst == "best":
            best_or_worst_cases.append(max(algo_orders, key=algo_orders.get))
        if best_or_worst == "worst":
            best_or_worst_cases.append(min(algo_orders, key=algo_orders.get))
    return best_or_worst_cases


def quadratic_plot(xpoints, akser):
    akser.plot(xpoints, (2**xpoints*2**xpoints)/10**8, label="Quadratic")


def nlogn_plot(xpoints, akser):
    akser.plot(xpoints, (2**xpoints*np.log2(2**xpoints)+1)/10**6, label="nlogn")
    print(xpoints)
    print(2**xpoints)


def linear_plot(xpoints, akser):
    akser.plot(xpoints, xpoints, label="Linear", marker='o')
    print(xpoints)
    print(xpoints)


if __name__ == "__main__":
    plot_time_datasize(data, data_labels, "sorted")
    plot_time_datasize(data, data_labels, "reversed")
    plot_time_datasize(data, data_labels, "random")
    plot_time_datasize(data, data_labels, "best_case")
    plot_time_datasize(data, data_labels, "worst_case")
    
