#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#define Songlist_Max 100

typedef struct songlist
{
	char name[30];
	char singer[30];
	int time;
	struct songlist *next;
}songlist;
void Randomplay();	//隨機撥放的功能
void Search();		//查詢輸入的演唱者總共有哪些歌曲
void Showallsong();	//排序
void Add();
void Delete();
void Modify();		//修改系統內的歌曲
int main(int argc, char *argv[])
{
	int a;
	songlist *s;
	songlist *ptr;
	songlist *head;
	songlist *save;
	songlist *cur;
	songlist *tail;
	songlist *new_node;
	FILE* fp;
	
	if (argc < 1)
	{
		fp = stdin;
	}
	else 
	{
		fp = fopen("songlist.csv", "rt");
		if (!fp) 
		{
			fprintf(stderr, "file %s not found\n", argv[1]);
			exit(1);
		}
	}
	s = (songlist *)malloc(sizeof(songlist)*(Songlist_Max));
	free(s); 
	char songlist[Songlist_Max];
    char *result = NULL;
    int i=0,n;
    fscanf(fp,"%d",&n);
    int c = 0;
   
        
	do{	
		
		new_node = (struct songlist *)malloc(sizeof(songlist));
		i++;
    	if(c == 0)
    	{	
	
    		head = new_node;
    		cur = new_node;
    		head = cur;
    		fscanf(fp,"%[^,] , %[^,] , %d",cur->name, cur->singer, &cur->time);		
    		c++;
		}
		else
		{	
			cur->next = new_node;
			cur = cur->next;
			fscanf(fp,"%[^,] , %[^,] , %d",cur->name, cur->singer, &cur->time);	
			
			if(cur->name==NULL || cur->singer==NULL || cur->time==0)//end of data 
			{
				cur->next=NULL;
				tail = cur;
				break;
			} 
			c++;		
    	}		
	}while(fgets(songlist,100, fp) != NULL);
	save = head;
	cur = head;	
	printf("\n共有%d首歌曲",c);
	printf("\n\n\n");
		while(cur!=tail)
	{

		printf(" Name = %s, Singer = %s, Time: %d\n", cur->name,cur->singer,cur->time);
		cur= cur->next;
	}
	printf("\n\n");
	printf("please choose a function:Add Delete Modify Search Showallsong Randomplay\n");
	char functionlist[6][20] = {"Add","Delete","Modify","Search","Showallsong","Randomplay"};
	char function[15];
	gets(function);
	if(strcmp(function,functionlist[0])== 0)
    {
    	Add();
	}
	else if(strcmp(function,functionlist[1])== 0)
    {
    	Delete();
	}
	else if(strcmp(function,functionlist[2])== 0)
    {
    	Modify();
	}
	else if(strcmp(function,functionlist[3])== 0)
    {
    	Search(*save,*tail,c);
	}
	else if(strcmp(function,functionlist[4])== 0)
    {
    	Showallsong(*save,c);
	}
	else if(strcmp(function,functionlist[5])== 0)
    {
    	Randomplay(*save,c);
	}
	else
	{
		printf("Error !!!\n");
		return;
	}
	
	
	
	
	
		
	
}
void Randomplay(songlist *start, int c)
{
	srand(time(NULL));
	songlist *name[800] = {NULL};
	songlist *singer[800]= {NULL};
	int *time[800]= {NULL};
	songlist *head;
	head = start;
	int i , a = 0 , random = 0;
	do{
	//for(i = 0 ; i<12000; i++){
		random = rand()%c;
		if( name[random] == NULL)
		{
			name[random] = head->name;
			singer[random] = head->singer;
			time[random] = head->time;
			head = head->next;
			a++;
		}
		
	}while(a!=c);
	printf("----------------------------------------------------------------------------------------------------------------------------------------------\n");
	for(i=0 ; i<c ;i++){

		
		printf("歌序: %3d | 歌曲名稱: %52s | 歌手名稱: %30s | 歌曲長度: %10d |\n",i,name[i],singer[i],time[i]);
		printf("----------------------------------------------------------------------------------------------------------------------------------------------\n");
	}
	
	
	
	
}
void Search(songlist *start,songlist *end,int c)
{
	char singer[20];
	int i;
	songlist *head;
	songlist *tail;
	songlist *cur;
	songlist *new_node;
	head = start;
	tail = start;
	//printf("您選擇的功能是演唱者查詢\n");
	int flag =0;
	
	
	printf("請輸入演唱者: ");
	//getchar();
	//scanf("%s",singer);
	gets(singer);
	while(head!=NULL)
	{
		if(strcmp(head->singer,singer)==0)
		{
			if(flag==0)
			{
				
				printf("%s 的歌曲有: \n",singer);
			
				
				for(i =0 ; i<c ; i++)
			{
				if(strcmp(head->singer , tail->singer) ==0)
				{
						printf("_____________________________________________\n");
						printf("|NO.|Song               |Singer      |Time  |\n");
						printf("_____________________________________________\n");
					    printf("    |%s     %s %d   \n",tail->name,tail->singer,tail->time);
					    printf("_____________________________________________\n");
					
				}
			        tail=tail->next;
		    }
				
				
                                flag=1;
                             
                                return;
			}
                  
        }
        	
			
            head=head->next;  
	
	}		
			
	
		if(head==NULL && head==0)
		{
			printf("沒有此演唱者的歌曲紀錄!\n");
			return;
		}
		return ;
	}

void floatUp2(struct songlist *head,int n)
{	
	//struct songlist *taill=head;
	
	struct songlist *tmp=head;
	struct songlist *curr=head;
	struct songlist *prev=head;
	
	int i,j;
	
	for(i=n ; i>0 ; i--)
	{
		curr=head;
		prev=head;
		for(j=0 ; j<i-1  && curr->next ; j++)
		{
			if(strncmp(curr->singer,curr->next->singer,10)>0)
			{
				tmp=curr->next;
				curr->next=tmp->next;
				tmp->next=curr;
				
				
				    
				if(curr==head)
				{
					head=tmp;
					prev=tmp;
				}
				else
				{
					prev->next=tmp;
					prev=prev->next;
				}
			}
			else
			{
				curr=curr->next;
				if(j!=0)
				{
					prev=prev->next;
				}
			}
			
		}
	}	
	for(i=0 ; i<n ;i++){
		printf("歌序: %3d | 歌曲名稱: %52s | 歌手名稱: %30s | 歌曲長度: %10d |\n",i,prev->name,prev->singer,prev->time);
		printf("----------------------------------------------------------------------------------------------------------------------------------------------\n");
		prev= prev->next;
	}	
}

void Showallsong(struct songlist *head,int n)
{

	struct songlist *tmp=head;	//暫存區
	struct songlist *curr=head;
	struct songlist *prev=head;	
	int i,j;
	
	for(i=n ; i>0 ; i--)		//跑n*n次
	{
		curr=head;				//存前幾筆已排好的資料，拿來當作比對
		prev=head;
		for(j=0 ; j<i-1  && curr->next ; j++)
		{
			if(strncmp(curr->name,curr->next->name,1)>0)	//比基準點小，交換
			{
				tmp=curr->next;
				curr->next=tmp->next;
				tmp->next=curr;
				    
				if(curr==head)
				{
					head=tmp;	//更新比對的資料
					prev=tmp;
				}
				else			//假設curr在比大小前，前幾筆資料是已經排好的
				{
					prev->next=tmp;
					prev=prev->next;
				}
			}
			else					//一樣or比基準點大
			{
				curr=curr->next;	//基準點移動
				if(j!=0)
				{
					prev=prev->next;
				}
			}
			
		}
	}	
	floatUp2(prev,n);
}

void Add()
{
	char singer[30];
	char name[30];
	int time;
	char a,b;
	int flag =0;	
	char data[150];
	int sure;
	printf("Enter the song data (name, singer, time)\n");
    gets(data);
    printf("Are you sure ?? Yes = 1 ; No = 0\n");
    scanf("%d",&sure);
    if(sure != 1)
    {
    	return;
	}
    else
	{
		FILE *fp;
    	fp = fopen("songlist.csv","a+");

		if(fp != NULL)
		{
			fputs(data,fp);
		    fprintf(fp,"\n");	
		}       
	    else 
		{
			printf("File Error !\n");
		}
		
	fclose(fp);
	printf("Add Success！\n");
	}
	
	readfile();	

}
void Delete()
{
	char deldata[150];
	char newlistarr[1000000];
	printf("Input the song data which you want delete:(name, singer, time)\n");
	gets(deldata);
	strcat(deldata,"\n");
	
	char linedata[200];
	
	FILE *fp;
	fp = fopen("songlist.csv","r");
	
	while(fgets(linedata,200,fp)!=NULL)
	{
		if(strcmp (linedata, deldata) != 0)
		{
			strcat(newlistarr, linedata);	
		}	
	}
	fclose(fp);
	
	fp = fopen("songlist.csv", "w");
	fputs(newlistarr,fp);
	
	printf("Delete Success");
	fclose(fp);
	readfile();
}
readfile()
{
	FILE *fp;

	songlist *s;
	songlist *ptr;
	songlist *head;
	songlist *save;
	songlist *cur;
	songlist *tail;
	songlist *new_node;
	
	fp = fopen("songlist.csv", "rt");


	s = (songlist *)malloc(sizeof(songlist)*(Songlist_Max));
	free(s); 
	char songlist[Songlist_Max];
    char *result = NULL;
    int i=0,n;
    fscanf(fp,"%d",&n);
    int c = 0;
       
	do{	
		
		new_node = (struct songlist *)malloc(sizeof(songlist));
		i++;
    	if(c == 0)
    	{	
	
    		head = new_node;
    		cur = new_node;
    		head = cur;
    		fscanf(fp,"%[^,] , %[^,] , %d",cur->name, cur->singer, &cur->time);  		
    		c++;
		}
		else
		{	
			cur->next = new_node;
			cur = cur->next;
			fscanf(fp,"%[^,] , %[^,] , %d",cur->name, cur->singer, &cur->time);	
			
			if(cur->name==NULL || cur->singer==NULL || cur->time==0)//end of data 
			{
				cur->next=NULL;
				tail = cur;
				break;
			} 
			c++;		
    	}		
	}while(fgets(songlist,100, fp) != NULL);
	printf("\n共有%d首歌曲",c);
	printf("\n\n\n");
	save= head;
	while(save!=tail)
	{
		printf(" Name = %s, Singer = %s, Time: %d\n", save->name,save->singer,save->time);
		save= save->next;
	}
}

void Modify()
{
	char singer[100];
	char songinfo[150];
	char songinfo_cp[150];
	char new_songinfo[150];
	char *songinfo_cut = NULL;
	char modify[10];
	char modify_list[3][10]={"name","singer","time"};
	char itoatime [5];
	songlist modifyinfo[1];
	
	printf("Enter the song info to be modified:\n");
	gets(songinfo);
	strcat(songinfo,"\n");
	puts(songinfo);
	strcpy(songinfo_cp,songinfo);	
	songinfo_cut = strtok(songinfo,",");
		int x = 0;
		while(songinfo_cut != NULL)
		{
			if(x==0)
			{
				strcpy(modifyinfo[0].name,songinfo_cut);
				x++;
			}
			else if(x==1)
			{
				strcpy(modifyinfo[0].singer,songinfo_cut);
				x++;
			}
			else if(x==2)
			{
				modifyinfo[0].time = atoi(songinfo_cut);
			}
			songinfo_cut = strtok(NULL, ",");
		}
	printf("Name = %s , Singer = %s , Time = %d\n",modifyinfo[0].name, modifyinfo[0].singer, modifyinfo[0].time);
	
	printf("What infor do you want to modify ? name ? singer ? time? ");
	gets(modify);
	
	
	printf("New Info: ");
	itoa(modifyinfo[0].time,itoatime,10);
	
	if(strcmp(modify, modify_list[0]) == 0)
	{
		gets(modifyinfo[0].name);
		printf("name: %s\n",modifyinfo[0].name);
	}
	else if(strcmp(modify, modify_list[1]) == 0)
	{
		gets(modifyinfo[0].singer);
		printf("singer: %s\n",modifyinfo[0].singer);
	}
	else if(strcmp(modify, modify_list[2]) == 0)
	{
		scanf("%d",&modifyinfo[0].time);
		printf("time: %d\n",modifyinfo[0].time);
		itoa(modifyinfo[0].time,itoatime,10);
	}
	
	strcat(new_songinfo,modifyinfo[0].name);
    strcat(new_songinfo,",");
    strcat(new_songinfo,modifyinfo[0].singer);
	strcat(new_songinfo,",");
    strcat(new_songinfo,itoatime);
    strcat(new_songinfo,"\n");
    
    char linedata[200];
    char newlistarr[1000000];
	
	FILE *fp;
	fp = fopen("songlist.csv","r");
	
	while(fgets(linedata,200,fp)!=NULL)
	{
		if(strcmp(linedata, songinfo_cp)== 0)
		{
			strcat(newlistarr, new_songinfo);	
		}
		else
		{
			strcat(newlistarr, linedata);	
		}		
	}
	fclose(fp);
	
	fp = fopen("songlist.csv", "w");
	fputs(newlistarr,fp);
	
	printf("Modify Success");
	fclose(fp);
	readfile();

	
    
  
		
} 
