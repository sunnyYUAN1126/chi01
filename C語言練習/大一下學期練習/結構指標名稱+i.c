#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,m,ff;
	struct date
	{
		int a;
		char arr[10];
	}stry[5]={ {20,"sss"},{5,"ttt"},{54,"ccc"},{30,"fgfd"},{5,"yuu"} };
	m=stry->a;
	for(i=0;i<5;i++)
	{
		if( ( (stry+i)->a )>m )
		{
			m=(stry+i)->a;
			ff=i;
		}
	}
	printf("%s,%d\n",(stry+ff)->arr,(stry+ff)->a);


}







