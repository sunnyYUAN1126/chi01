#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a,b;
	char ch;

	printf("輸入運算式: ");
	scanf("%d %c %d",&a,&ch,&b);

	switch(ch)
	{
		case '+':
			printf("%d %c %d=%d\n",a,ch,b,a+b); //用%c ch
			break;

		case '-':
			printf("%d - %d=%d\n",a,b,a-b); //直接用減
			break;

		case '*':
			printf("%d * %d=%d\n",a,b,a*b);
			break;

		case '/':
			printf("%d / %d=%.3f\n",a,b,(float)a/b);
			break;
		default:
			printf("錯誤\n");
	}
}

