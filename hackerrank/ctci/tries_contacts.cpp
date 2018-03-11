/*
We're going to make our own Contacts application! The application must perform two types of operations:

    1. add name, where name is a string denoting a contact name. This must store name as a new contact in the application.
    2. find partial, where partial is a string denoting a partial name to search the application for.
    It must count the number of contacts starting with partial and print the count on a new line.

Given n sequential add and find operations, perform each operation in order.

*/

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

const int ALPHABET_SIZE = 26;

struct TrieNode
{
  struct TrieNode* children[ALPHABET_SIZE];
  int numWords;
  bool isEndOfWord;
};

struct TrieNode* getNode()
{
  struct TrieNode* pNode = new TrieNode;
  pNode->isEndOfWord = false;
  pNode->numWords = 0;
  for(int i=0;i<ALPHABET_SIZE;i++) pNode->children[i] = NULL;
  return pNode;
}

void insert(TrieNode* root,string value)
{
  struct TrieNode* pcrawl = root;
  for(int i=0;i<value.length();i++)
  {
    int index = value[i] - 'a';
    if (!pcrawl->children[index])
    {
      pcrawl->children[index] = getNode();
    }
    pcrawl = pcrawl->children[index];
    pcrawl->numWords +=1;
  }
  pcrawl->isEndOfWord = true;
}
int searchWords(TrieNode* root,string search)
{
  TrieNode* pcrawl = root;
  for(int i=0;i<search.length();i++)
  {
    int index = search[i] - 'a';
    if(!pcrawl->children[index])
      return 0;
    pcrawl = pcrawl->children[index];
  }
  return pcrawl->numWords;
}


int main()
{
  ofstream myfile;
  myfile.open("myoutput.txt");
  int t;
  cin>>t;
  cin.ignore();
  TrieNode *root = getNode();
  while (t>0)
  {
    string inst,word;
    getline(cin,inst);
    if (inst.find("add")!=-1)
    {
      word = inst.substr(inst.find(' ')+1);
      // cout<<word<<"\n";
      insert(root,word);
    }
    else if(inst.find("find")!=-1)
    {
      word = inst.substr(inst.find(' ')+1);
      // cout<<word;
      int numWords = searchWords(root,word);
      cout<<numWords<<"\n";
      myfile<<numWords<<"\n";
    }
    t--;
  }
  myfile.close();
}
