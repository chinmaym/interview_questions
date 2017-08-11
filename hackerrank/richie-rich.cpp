#include<iostream>
#include<ctime>
using namespace std;
int check(char a[],char b[]){
	int first[26] = {0},second[26] = {0},c=0;
	while(a[c]!='\0'){
		first[a[c]-'a']+=1;
		c++;
	}
	c=0;
	while(b[c]!='\0'){
		second[b[c]-'a']+=1;
		c++;
	}
	for(c=0;c<26;c++){
		if(first[c]!=second[c]){
			return 0;
		}
	}
	return 1;

}

int main()
{
	int t;
	cin>>t;
	while(t>0){
		const clock_t begin_time = clock();
		char s[100];
		char sub1[100]={0};
		char sub2[100]={0};
		scanf("%s",s);
		int count =0;
		for(int len =1;len<strlen(s);len++)
		{
			memset(sub1,0,len);
			for(int i=0;i<strlen(s)-len;i++)
			{
				//printf("%s\n",sub1);
				strncpy(sub1,&s[i],len);
				memset(sub2,0,len);
				for(int j=i+1;j<strlen(s)-len+1;j++)
				{
					//printf("%s\n",sub2);
					strncpy(sub2,&s[j],len);
					if(check(sub1,sub2)==1){
						//printf("%s---------%s\n",sub1,sub2);
						count+=1;
					}
				}

			}
		}
		//printf("%d\t%f\n",count,float(clock() - begin_time));
		printf("%d\t%f\n",count);
		t--;
	}
	return 0;
}