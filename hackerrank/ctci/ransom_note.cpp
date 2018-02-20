/*
A kidnapper wrote a ransom note but is worried it will be traced back to him.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
*/

#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;


bool ransom_check(vector<string> ransom, vector<string> magazine)
{
  unordered_map<string,int> umap;
  for(const auto& i:ransom) umap[i] +=1;
  for(const auto& i:magazine) if(umap[i]>0) umap[i] -= 1;
  for(const auto& i:umap) if (i.second > 0) return false;
  return true;
}



int main(){
  int n,m;
  cin>>m>>n;
  vector<string> magazine(m);
  for(int i =0;i<m;i++){
    cin>>magazine[i];
  }
  vector<string> ransom(n);
  for (int i = 0; i < n; i++) {
    cin>>ransom[i];
  }
  if (ransom_check(ransom,magazine)) cout<<"Yes\n";
  else cout<<"No\n";
  return 0;
}
