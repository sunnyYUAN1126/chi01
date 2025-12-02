#include<stdio.h>
int ccc(int a,int b);
int main()
{
	int c=54;
	int d=ccc(11,c);
	printf("%d",d);
}

int ccc(int a,int b)
{ 
	printf("%d,%d\n",a,b);
        int c=b/a; 
	return c;
}
