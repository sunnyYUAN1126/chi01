#include<stdio.h>
#include<stdlib.h>
void diamond(int nn);
void upper(int nn);
void lower(int nn);
void put(char cc,int  nn);
int main(void)
{
	int nn=3;
	diamond(nn);

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
}
