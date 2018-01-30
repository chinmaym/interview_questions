/*
string "aabcc" would become either "aab" or "bcc" after operation.
Sample Input 0
aaabccddd
Sample Output 0
abd
*/
#include <bits/stdc++.h>

using namespace std;

//--------------------------------------Best Solution------------------------------
string super_reduced_string(string s){
  vector<char> ans;
  for(int i=0;i<s.length();i++){
    if(ans.size()==0 or ans.back()!=s[i]) ans.push_back(s[i]);
    else ans.pop_back();
  }
  if (ans.size() == 0) return "Empty String";
  else{
    string ret(ans.begin(),ans.end());
    return ret;
  }
}


//---------------------------------------My Solution--------------------------------
/*string super_reduced_string(string s){
    int flag = 1,i;
    char *p = new char[s.length()];
    char *t = new char[s.length()];
    strcpy(t,s.c_str());
    // printf("t=%s\n",t);
    while(flag == 1)
    {
        flag = 0;
        int j=0;
        for(i=0;t[i]!='\0';i++ )
        {
            if(t[i] != t[i+1])
            {
                // printf("Here comes\n");
                p[j++] = t[i];
            }
            else
            {
              flag = 1;
              // printf("i=%d\n",i );
              i+=1;
            }
        }
        p[j]='\0';
        // printf("p=%s\n",p);
        for(i=0;p[i]!='\0';i++)
        {
          t[i] = p[i];
        }
        t[i]='\0';
        // printf("t=%s\n",t);
    }
    if(p[0]=='\0')
    {
      return "Empty String";
    }
    return p;
}*/
int main() {
    string s;
    cin >> s;
    string result = super_reduced_string(s);
    cout << result << endl;
    return 0;
}
