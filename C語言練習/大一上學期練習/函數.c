#include<stdio.h>
#include<stdlib.h>
void fun1(int i);
void fun2(int i);
int main(void)
{
	int a;
	scanf("%d",&a);
	printf("顆顆\n"); 
	for( a ;a>0;a--) {		
		fun1(a);
		fun2(a);  
	}
       
	return 0;
}

void fun1(int i)
{
	int b;
	for(b=0;b<i;b++) {
		printf("*");
	}

	printf("\n");
	return;
}

void  fun2(int i)
{
	int b;
	for(b=0;b<i;b++) {
		printf("*");
	}

	printf("\n");
	return;
}



		

