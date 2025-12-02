#include<stdio.h>
#include<stdlib.h>
int main(void)

/*
{
	int a=0,i=1;
	do{
		a+=i++;
         }while(i<=10);
		 printf("%d",a);
		 return 0;
}






{
	int a=10,i=1;
	while(i<=10)
	{
		a+=i++;
	printf("%d\n",a);}

}


*/

{
	int a=0,i=1;
	for(i;i<=10;i++)	
	a+=i++;
	printf("%d\n",a);
       
}

