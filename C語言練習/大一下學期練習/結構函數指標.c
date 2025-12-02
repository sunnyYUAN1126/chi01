#include<stdio.h>
#include<stdlib.h>
struct date
{
	int a;
	char arr[10];
};
int fun(struct date  *);
int main(void)
{
	struct date stry={77,"gfgf"};
	fun(&stry);
}
int fun(struct date *bby)
{
	printf("%d,%s\n",bby->a,bby->arr);
}
	










