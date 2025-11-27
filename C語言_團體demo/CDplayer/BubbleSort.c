#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define Songlist_Max 100

typedef struct songlist
{
	char name[30];
	char singer[30];
	int time;
	struct songlist *next;
}songlist;



void floatUp2(struct songlist *head,int n)
{
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
			
			//strcmp(curr->singer,curr->next->singer)>0
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
	for(i=0 ;i<n; i++)
    {
    	
		printf("%-20s\t %-20s\t %-20d\t\n", prev->name, prev->singer,prev->time);	
		prev= prev->next;
	}		
}

void floatUp1(struct songlist *head,int n)
{

	struct songlist *tmp=head;
	struct songlist *curr=head;
	struct songlist *prev=head;
	struct songlist *team;

	int i,j;
	
	for(i=n ; i>0 ; i--)
	{
		curr=head;
		prev=head;
		for(j=0 ; j<i-1  && curr->next ; j++)
		{
			if(strncmp(curr->name,curr->next->name,1)>0)
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
	team=prev;	
	for(i=0 ;i<n; i++)
    {
    	
		printf("%-20s\t %-20s\t %-20d\t\n", prev->name, prev->singer,prev->time);	
		prev= prev->next;
	}	
	printf("\n");
	printf("-----------------------------------------------------\n");
	printf("bubble sort 2(singer): \n\n");
	
	floatUp2(team,n);
}



















    




int main(int argc, char *argv[])
{
	songlist *s;
	songlist *ptr;
	songlist *head;
	songlist *cur;
	songlist *tail;
	songlist *new_node;
	songlist *songgg;
	FILE* fp;
	
	if (argc < 1)
	{
		fp = stdin;
	}
	else 
	{
		fp = fopen("songlist15.csv", "rt");
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
		//	printf("Song[%3d] Name: %s\n Singer: %s\n Time: %d\n", i, cur->name, cur->singer, cur->time);   		
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
			
		//	printf("Song[%3d] Name: %s\n Singer: %s\n Time: %d\n", i, cur->name,cur->singer, cur->time);
			c++;		
    	}		
	}while(fgets(songlist,100, fp) != NULL);
	printf("\ntotal=%d",c);  //¦@¦³c­ººq¦±

	printf("\n\n\n");
	

	
	songgg=head;
	
	
	while(head!=tail)
    {
    	
		printf("%-20s\t %-20s\t %-20d\t\n", head->name, head->singer,head->time);	
		head= head->next;
	}
	printf("\n");
	printf("-----------------------------------------------------\n");
	printf("bubble sort 1(name): \n\n");
	
	
	
	
	
	
	floatUp1(songgg,c);
}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
