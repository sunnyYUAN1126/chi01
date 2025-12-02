#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i;
	struct date
	{
		int a;
		char arr[10];
	}stry={22,"sunny"},*ptr;
	ptr=&stry;

	printf("%d\n",ptr->a);
	printf("%s\n",stry.arr);
}







