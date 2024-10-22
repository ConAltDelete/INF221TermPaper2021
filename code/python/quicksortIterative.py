from numba import jit

@jit(nopython=True)
def swap(A:list, i:int, j:int):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

@jit(nopython=True)
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

@jit(nopython=True)
def partision_mod(A:list, p:int, r:int):
    mid = (p+r)//2

    if A[mid] < A[p]:
        swap(A,mid,p)
    if A[r] < A[p]:
        swap(A,r,p)
    if A[mid] < A[r]:
        swap(A,r,mid)

    x = A[r]
    i = p
    gt = r
    lt = p
    while i <= gt:
        if A[i] == x:
            i += 1
        elif A[i] < x:
            swap(A,lt,i)
            lt += 1
            i += 1
        elif A[i] > x:
            swap(A,gt,i)
            gt -= 1
    return (gt+lt)//2
    
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
@jit(nopython=True)
def quicksortIterative(arr, l=-2, h=-2):
    if l < -1:
        l = 0
    if h < -1:
        h = len(arr) - 1

    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partision_mod(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above
if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
