#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main(void)
{
	int pp,cc,a,z;
	char *arr[14]={"二校宿舍","澄清醫院公車站","公車ing","朝馬公車站",
		"統聯轉運站","客運衝衝衝","台北轉運站","台北火車站",
		"松山火車站","南港火車站","汐科火車站","機車上路",
		"社區","到家"};
	srand(time(NULL));

	while(z<=14 || a<=14)
	{
	getchar();
	
	pp=((rand()%6)+1);
	a+=pp;
	printf("走%d步,玩家位置\"%s\"\n",pp,arr[a]);
	
	cc=((rand()%6)+1);
	z+=cc;
	printf("走%d步,電腦位置\"%s\"\n",cc,arr[z]);
	
	
	}
}


