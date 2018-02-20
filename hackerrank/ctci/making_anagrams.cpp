/*
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams.
Can you help her find this number?

Given two strings, and , that may or may not be of the same length, determine the minimum number of character deletions required to make and anagrams.
Any characters can be deleted from either of the strings.

Sample Input

cde
abc

Sample Output

4

Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

    Remove d and e from cde to get c.
    Remove a and b from abc to get c.
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int number_needed(string a, string b) {
  unordered_map<char,int> u;
  for(const auto& n:a){
    u[n] += 1;
  }
  for(const auto& n:b){
    u[n] -= 1;
  }
  auto sum = 0;
  for(const auto& n:u){
    if(n.second < 0){
      sum += -1 * n.second;
    }
    else{
      sum+=n.second;
    }
  }
  return sum;
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}
