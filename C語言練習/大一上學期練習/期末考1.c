#include<stdio.h>
#include<stdlib.h>
int fun1(int);
int fun2(int);
int fun(char,int);
int main(void)
{
	int i,nn;
	scanf("%d",&nn);
	fun1(nn);
	fun2(nn);
}
int fun1(int nn)
{
	int i;
	for(i=1;i<=nn;i++){
		fun(' ',nn-i);
		fun('*',2*i-1);
		printf("\n");
	}
}

int fun2(int nn)
{
        int i;
	for(i=1;i<nn;i++){
                fun(' ',i);
                fun('*',2*nn-2*i-1);
                printf("\n");
        }
}

int fun(char ch,int nn)
{
	int i;
	for(i=1;i<=nn;i++){
		printf("%c",ch);
	}
}





