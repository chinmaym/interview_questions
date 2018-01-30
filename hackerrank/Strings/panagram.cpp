/*
Given a sentence s, tell Roy if it is a pangram or not.
Input #1
We promptly judged antique ivory buckles for the next prize

Input #2
We promptly judged antique ivory buckles for the prize

Sample Output
Output #1
pangram

Output #2
not pangram
*/
#include<cstdio>
using namespace std;

char const* checkPanagram(char* usrStr)
{
  int count[26] = {0},i;
  for(i=0;usrStr[i]!='\0';i++)
  {
    if (usrStr[i] == ' ')
    {
      continue;
    }
    if(usrStr[i]>=65 and usrStr[i]<=90)
    {
      printf("%d,%c = %d\n",i,usrStr[i],(usrStr[i]-65) );
      count[(usrStr[i]-65)] = 1;
    }
    else if(usrStr[i]>=97 and usrStr[i]<=122)
    {
      printf("%d,%c = %d\n",i,usrStr[i],(usrStr[i]-97) );
      count[(usrStr[i]-97)] = 1;
    }
  }
  int flag = 0;
  for(i = 0;i<26;i++)
  { printf("%d = %d\n",i,count[i]);
    if(count[i]==0)
    {
      flag = 1;
    }
  }
  if (flag==0)
  {
    return "pangram";
  }
  else{
    return "not pangram";
  }
}

int main()
{
  char *usrInput = new char[1000];
  fgets(usrInput,1000,stdin);
  // printf("%s\n",usrInput );
  printf("%s",checkPanagram(usrInput));
}
