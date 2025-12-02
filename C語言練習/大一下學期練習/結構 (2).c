#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	struct date
	{
		char arr[10];
	}stry[3]={{"ccc"},{"ddd"},{"ddw"}};

	printf("%s\n",stry[0].arr);
	printf("%s\n",stry[1].arr);


}


