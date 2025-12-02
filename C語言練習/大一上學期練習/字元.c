#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int num;
	char ch;

	printf("輸入整數: ");
	scanf("%d" , &num);
	
	fflush( stdin );
	
	printf("輸入字元:");
	scanf( "%c", &ch);
	printf("num=%d,ascii code of ch=%d\n",num ,ch);

	return 0;
}
