#include<stdio.h>
#include<stdlib.h>
void arrow(int nn);
void put(char cc,int  nn);
int main(void)
{
	int nn;
	printf("歡迎\n");
	scanf("%d",&nn);

	arrow(nn);
	return 0;
}

void arrow(int nn)
{
	int ii;
	for(ii=1;ii<=nn;ii++)
	{
		put(' ',nn-ii+1);
		put('*',ii);
		put('*',ii);
		printf("\n");
	}

	put('*',2*nn+2);
	
	printf("\n");
	for(ii=1;ii<=nn;ii++)
	{
		put(' ',ii);
		put('*',nn-ii+1);
		put('*',nn-ii+1);
		printf("\n");
	}
}

void put(char cc,int nn)
{
	int ii;
	for(ii=0;ii<nn;ii++)
	{
		printf("%c",cc);
	}

return;
}


			


