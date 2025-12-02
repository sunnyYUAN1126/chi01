#include<stdio.h>
#include<stdlib.h>
void arrow(int nn,int ll);
void diamond(int nn);
void upper(int nn);
void lower(int nn);
void put(char cc,int  nn);
int main(void)
{
	int nn;
	printf("歡迎\n");
	scanf("%d",&nn);

	arrow(nn, 4);
	diamond(nn);
	return 0;
}

void arrow(int nn,int ll)
{
	int ii;
	for(ii=1;ii<=nn;ii++)
	{
		put(' ',nn-ii+1);
		put('*',ll);
		printf("\n");
	}

	put('*',ll);
	printf("\n");

	for(ii=1;ii<=nn;ii++)
	{
		put(' ',ii);
		put('*',ll);
		printf("\n");
	}
}

void diamond(int nn)
{
	upper(nn);
	lower(nn);
}

void lower(int nn)
{
	int ii;
	for(ii=0;ii<=nn;ii++)
	{
	        put(' ',ii);
                put('*',nn-ii);
                printf("\n");
	}	
	
}

void upper(int nn)
{
	int ii;
	for(ii=0;ii<=nn;ii++)
	{
		put('*',ii);
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


			


