#include<stdio.h>
#include<stdlib.h>
void main(void)
{
	int a;
	printf("輸入今日心情(1-10):");
        scanf("%d",&a);
        if((a>0) && (a<11) )
	switch(a%10)
	{
		default:
	        printf("宅在家\n");
	        break;
		
		case 0:
		printf("出國玩\n");
		break;
		
		case 9:
		printf("去遊樂園\n");
		break;

		case 8:
		printf("玩母湯熊喔\n");
		break;

		case 7:
		printf("94要逛街\n");
		break;

		case 6:
		printf("看電影\n");
		break;
               
		}
	else
	printf("訊息錯誤,請輸入1-10\n");

}
