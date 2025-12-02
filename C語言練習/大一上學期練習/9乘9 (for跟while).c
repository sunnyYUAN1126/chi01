#include<stdio.h>
#include<stdlib.h>
int fun1(int,int);
int fun2(int,int);
int main(void)
{
	int i,j;
	fun1(i,j);
	printf("\n");
	fun2(i,j);
}

int fun1(int i,int j)
{
	for(i=1;i<10;i++) {
		for(j=1;j<10;j++) {
			printf(" %d*%d=%d\t",i,j,i*j); }
		printf("\n");
	}
}

int fun2(int i,int j)
{
	i=1;
//	j=1; j不行在這裡,會無法執行,因為它不在while裡面無法被累計
	while(i<10) {
                j=1;        // 在while裡面,當最裡面while的值出來,會帶進j累計
		while(j<10) {
			printf(" %d*%d=%d\t",i,j,i*j);
	                j++;
		}
		printf("\n");
		i++;
	}

}

