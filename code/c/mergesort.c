#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void merge(int* array, long p, long r, long q){
	long n1 = r-p+1;
	long n2 = q - r;

	int* L = malloc(sizeof(int)*(n1 + 1));
	int* R = malloc(sizeof(int)*(n2 + 1));
	
	for(long i = 0; i < n1; i ++) {
		*(L + i) = *(array + p + i -1);
	}
	for(long i = 0; i < n2; i ++) {
		*(R + i) = *(array + q + i);
	}



	free(L);
	free(R);
}

void mergesort(int* array, long p, long q){
	if(p < q){
		long r = floor((p+q)/2);
		mergesort(array,p,r);
		mergesort(array,r+1,q);
		merge(array,p,q,r);
	}
}

int main(){
	long size = pow(2,10);
	int* ptr = malloc(size);
	for(long i = 0; i < size; i++){
		*(ptr + i) = (int)(rand() % 10000);
	}
	mergesort(ptr,0,size-1);
}
