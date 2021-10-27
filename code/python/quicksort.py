from numba import jit

@jit(nopython=True)
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

@jit(nopython=True)
def partision(A, p, r):
	x = A[r]
	i = p -1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			swap(A,j,i)
	swap(A,i+1,r)
	return i +1 

@jit(nopython=True)
def quicksort(A: list, p = None,r = None):
	if p is None:
		p = 0
	if r is None:
		r = len(A)-1
	if p < r:
		q = partision(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)

if __name__ == "__main__":
	L = [1,4,2,6,7,8,3]
	quicksort(L,0,len(L)-1)
	print(L)
