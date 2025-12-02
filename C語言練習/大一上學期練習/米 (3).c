#include<stdio.h>
#include<stdlib.h>
void star(int i);
int main(void)
{
	int a;
	printf("歡迎\n");
	for(a=5;a>0;a--)
	{
		star(a);
                 
	}
		return 0;
}


 
void star(int i)
{
	int a;
	{
	for(a=0;a<i;a++)
	{ printf("*"); }
	}                                    

	printf("\n");
        return;
}
 


