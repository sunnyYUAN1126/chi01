#include<stdio.h>
#include<stdlib.h>
int fun(int *i);
int main(void)
{
	int a=3;
	int *c=&a;
      	
	printf("a值=%d    a地址=%p\n",a,&a);
	printf("c值=%d    c地址=%p\n",*c,c);
        fun(&a);
	printf("\n");
	printf("  c加&變成=&c\n" 
	       "  &c地址改變\n"
	       "  不是&a地址\n"
	       "  (i也一樣)\n");
	printf("\n");
	printf("c值=%d    c地址=%p\n",*c,&c);       	
	return 0;
}

int fun(int *i)
{
	*i=5;
	printf("i值=%d    i地址=%p\n",*i,i);
}



