#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a,b,c,d=333,t=1;   /* a=業者 ,b=銷費者 ,c=密碼變數 ,d=密碼 ,t=輸入次數 */
	printf("輸入身分(1為業主,2為消費者): ");
	scanf("%d",&a);

	if( (a==1) || (a==2)  )
	{

			if(a==1)   /* 業主 */
			{
			printf("輸入密碼: ");
			scanf("%d",&c); 


		while(t<6)
		{
	
	          if(c!=d)   /* 密碼不行 */
	          {
		       printf("密碼錯誤\n再輸入一次: ");
		       scanf("%d",&c);
		       t++;   /* 輸入錯誤5次 */
	          }
	


		  if(c==d)  /*密碼可以 */
	          
		  {    printf("1.列出商品\n2.進貨\n3.查看銷售\n4.修改密碼\n");   /* 下次要做進選單,用switch */
	               break;
		  }
		  
		}
		  
		            int e;  // e=選單 //
		            if(c==d)	    
			    {
				    printf("輸入想要的選單: ");
                                    scanf("%d",&e);
			            switch(e)
			            {
				    case 1:
				    printf("A商品\n");
				    printf("B商品\n");
				    break;
				    
				    case 2:
                                    printf("A商品\n");
				    printf("B商品\n");
				    break;
				   
				    case 3:
				    printf("A商品\n");
                                    printf("B商品\n");
                                    break;

				    case 4:
				    printf("修改中\n");
				    break;
			            }  	       
	   		        }
			    }

        
	else   /* 消費者 */
	 {  printf("列出所有商品\n");  }
        }
	else
         { printf("輸入錯誤\n");  }

	return 0;
}
	

