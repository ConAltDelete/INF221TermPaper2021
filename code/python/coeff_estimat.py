import numpy as np
import csv
def get_data(path):
    algos = ["numpy_sort","python_sort"]
    data = dict()
    for a in algos:
        csv_read_list = list()
        head = list()
        with open(path + a + ".csv") as csv_file:
            csv_read=csv.reader(csv_file, delimiter=',')
            head = next(csv_read)
            for row in csv_read:
                csv_read_list.append([float(e) for e in row])
        data[a] = {"head":head,"data":csv_read_list[1:]}

    return data

def mod_regrass(data,formula=[lambda x: 1, lambda x: x, lambda x: x**2]):
    """
        formula is a list of functions, data is a nx2 list
    """

    A = np.matrix([[f(d[0]) for f in formula] for d in data])
    y = np.matrix([[d[1]] for d in data])

    if len(data) >= len(data[0]):
        inv_A = (A.transpose()*A)**-1 * A.transpose()
    else:
        inv_A = A.transpose() * (A*A.transpose())**-1

    return inv_A*y

if __name__ == "__main__":
    f_list = [
                lambda x: 1,
                lambda x: np.log2(x),
                lambda x: x,
                lambda x: x*np.log2(x),
                lambda x: x**2,
                lambda x: x**3,
            ]
    data = get_data("./data/csv_files/")

    numpy_data = [[d[0] , d[5]] for d in data["numpy_sort"]["data"]]
    coffs = mod_regrass(numpy_data,f_list[:4])


    print(coffs)
