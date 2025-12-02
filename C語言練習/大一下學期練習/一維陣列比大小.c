#include<stdlib.h>
#include<stdio.h>
int main(void)
{
	int arr[6]={3,4,12,6,44,1};
	int max,min,chang;
	max=arr[0];
	min=arr[0];
	for(int i;i<6;i++)
	{
		if(max<arr[i]){
			chang=max;
			max=arr[i];
			arr[i]=chang;
		}

		if(min>arr[i]){
                        chang=min;
                        min=arr[i];
                        arr[i]=chang;
                }

	}
	printf("min=%d,max=%d\n",min,max);
}

			


