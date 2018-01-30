/*
Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following properties:

    It is a concatenation of one or more words consisting of English letters.
    All letters in the first word are lowercase.
    For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Sample Input
saveChangesInTheEditor
Sample Output
5
*/

#include<iostream>
using namespace std;


int getWordCount(char *a)
{
  int count = 1;
  for(int i=0;a[i]!='\0';i++)
  {
    if(int(a[i])>=65 and int(a[i])<=92)
    {
      // printf("%d\n",int(a[i]));
      count +=1;
    }
  }
  return count;
}

int main()
{
  char a[100000];
  cin>>a;
  printf("%d\n",getWordCount(a));
}
