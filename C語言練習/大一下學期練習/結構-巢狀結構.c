#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	struct date
	{
		char arr[10];
	};
	struct bate
	{
		int brr;
		struct date stry;
	}btry={333,{"ddd"} };
	printf("%d\n",btry.brr);
	printf("%s\n",btry.stry.arr);
}


