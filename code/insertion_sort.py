def insertion_sort(List: list):
    i = 1
    while i < len(List):
        temp = List[i]
        j = i - 1
        while j >= 0 and List[j] > temp:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = temp
        i += 1


if __name__ == "__main__":
    l = [0,6,1,2,9,0,3]
    insertion_sort(l)
    print(l)
