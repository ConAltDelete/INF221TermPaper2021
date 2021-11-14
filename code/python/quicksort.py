from numba import jit

@jit(nopython=True)
def swap(A:list, i:int, j:int):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

@jit(nopython=True)
def partision(A:list, p:int, r:int):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			swap(A,j,i)
	swap(A,i+1,r)
	return i +1 

@jit(nopython=True)
def quicksort(A:list, p = -1,r = -1):
	if p < 0:
		p = 0
	if r < 0:
		r = len(A)-1
	if p < r:
		q = partision(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)
