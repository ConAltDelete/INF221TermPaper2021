#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void swap(short int array[], unsigned int p, unsigned int r){
	double temp = array[p];
	array[p] = array[r];
	array[r] = temp;
}

double partition(int* array, unsigned int p, unsigned int r) {
	double x = *(array + r);
	double i = p - 1;
	for(unsigned int j = p; j<r ;j++){
		if(*(array + j) <= x){
			i++;
			swap(array,i,j);
		}
	}
	swap(array, i+1, r);
	return i + 1;
}

void quicksort(int* array, unsigned int p, unsigned int r){
	if(p<r){
		double q = partition(array,p,r);
		quicksort(array,p,q-1);
		quicksort(array,q,r);
	}
}

int main() {
	unsigned int size = (unsigned int) pow(2,8);
	printf("%i\n",size);
	ptr = (unsigned int*) malloc(sizeof(unsigned int)*size);

	if(ptr == NULL){
		printf("Memmory did not allocate.");
		exit(1)
	}

	for(unsigned int i = 0; i < size; i++){
		int* address = ptr + i;
		address = (unsigned int)(rand() % 1000);
		printf("%i,", *(ptr+i));
	}
	printf("\n");
	quicksort(array,0,size-1);
	free(ptr);
	for(unsigned int i = 0; i< size; i++){
		printf("%i,",array[i]);
	}
}
