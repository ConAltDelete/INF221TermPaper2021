from numba import jit

#@jit(nopython=True)
def swap(A:list, i:int, j:int):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

#@jit(nopython=True)
def partision(A:list, p:int, r:int):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			swap(A,j,i)
	swap(A,i+1,r)
	return i +1 

#@jit(nopython=True)
def partision_mod(A:list, p:int, r:int):
    x = A[p]
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

#@jit(nopython=True)
def quicksort(A:list, p = -2,r = -2):
	if p < -1:
		p = 0
	if r < -1:
		r = len(A)-1
	if p < r:
		q = partision_mod(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)


if __name__ == "__main__":
    l = [5,5,5,5,5,5,5,5,5,5,5]
    quicksort(l)
    print(l)
