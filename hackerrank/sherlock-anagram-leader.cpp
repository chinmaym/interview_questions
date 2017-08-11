#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool CheckAna(string & s, int start1, int start2, int len)
    {
    int let[26] = {0};
    bool result = true;
    for (int n = 0; n < len; n++)
        {
        let[s[start1+n]-'a']++;
        let[s[start2+n]-'a']--;
    }
    for (int n= 0; n <26; n++)
        {
        if (let[n] != 0)
            {
            result = false;
            break;
        }
    }
    return result;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;
    for (int total = 0; total < T; total++)
        {
        string stringin;
        int arr[128] = {0};
        cin >> stringin;
        int count = 0;
        for (int n = 0; n < stringin.length(); n++)
            arr[stringin[n]]++;

        // Reduce string with unnecessary chars which do not repeat in sequence
        // These don't affect final outcome since pAp is the same as pABCp for finding pA/Ap or pABC/ABCp

        string str = "";

        int last = -1;
        for (int n = 0; n < stringin.length(); n++)
            {
            if ((arr[stringin[n]] != last) || arr[stringin[n]] > 1)
                {
                str = str+stringin[n];
            }
            last = arr[stringin[n]];
        }
        
        string keyletters = "";
        // Now create keyletters with chars that appear more than once in order of appearance
        for (int n = 0; n < str.length(); n++)
            {
            if ((arr[str[n]] > 1) && (keyletters.find(str[n]) == string::npos))
                {
                keyletters += str.substr(n,1);
            }
        }
        
        
        int uaps = 0;            //Count of unordered anagrammatic pairs
        // Now for each recurring char
        for (int rc = 0; rc < keyletters.length() ; rc++)
            {
            //First add individual matches
            uaps += ((arr[keyletters[rc]]* (arr[keyletters[rc]]-1))/2);
/*            cout << endl << "LETTER:  " << keyletters[rc] << endl;
            cout << " uaps: " << uaps << endl;*/
            
            //Now build array of positions of this char in the string
            int pos[arr[keyletters[rc]]] = {-1};
            int t = -1;
            for (int n = 0 ; n < arr[keyletters[rc]]; n++)
                {
                pos[n] = str.find (keyletters[rc],t+1);
                t = pos[n];
            }
            //For all possible pairs of this char
            for (int n1 = 0; n1 < arr[keyletters[rc]] -1; n1++)
                {
                for (int n2 = n1+1 ; n2 < arr[keyletters[rc]]; n2++)
                    {
                    int lf = pos[n1];       //Position of left of pair
                    int rt = pos[n2];       //Position of right of pair
            
                    int distance = rt-lf;
                    //If separated by at least one char
                    if (distance > 1)
                        {
                        // Find inner matches (up to but not including both ends)
                        for (int x1 = 1; x1 < distance; x1++)
                            {
                            if (CheckAna(str, lf, rt-x1, x1+1))
                                uaps++;
                        }
//                        cout << "   after std inner match uaps: " << uaps << endl;
                        // Find mixed (inner partial) + outer matches (only towards the right!)
                        // But first find right outer bound for matches
                        
                        // Right outer bound:
                        //   Stop when: reached end of string
                        //   Non repeating char found
                        //   Same char as one under consideration -->> will be processed in a later iteration
                        int rlimit = 0;         //Will be positive offset
                        for (rlimit = rt+1; rlimit < str.length(); rlimit++)
                            {
                            // If I hit non repeating char or I hit another char like current keyletter
                            if ((arr[str[rlimit]] < 2) || (str[rlimit] == keyletters[rc]))
                                {
                                rlimit --;
                                break;
                            }
                        }
                        // Check for right overflow
                        if (rlimit >= str.length())
                            rlimit = str.length()-1;
                        // If there's something more to the right then attempt matches
                        if (rlimit > rt)
                            {
                            
                            // If the outer bound is more than 0 then check for inner right bound
                            int llimit = 0;
/*                            int nonrepcharcount = 0;
                            for (llimit = rt-1; llimit == lf+rlimit; llimit--)
                                if ((arr[str[llimit]] < 2))     //Only check for non repeating chars
                                //Anything else is ok
                            {
                                nonrepcharcount++;
                                if (nonrepcharcount > 1)      //If this is the second non repeating char
                                                              //   I've hit my limit (one is OK, more than that NO)
                                    {
                                    llimit++;
                                    break;
                                }
                            }
*/
                            llimit = lf+1;

                            //OK now I know how far I can go to the left (from rt position) and how far to the outer right
                            // Check possible candidates
//                            cout << "len: " << str.length() << "  LL: " << llimit << "  RL: " << rlimit << endl;
                            for (int x1 = llimit; x1 <= rt; x1++)   //Possible left edges of right anagram
                                                                    //up to and including rt
                                {
                                for (int x2 = rt+1; x2 <= rlimit; x2++ )
                                        //Possible right edges at least one char to the right of rt
                                        //Up to and including rlimit
                                    {
/*                                    cout << "x1: " << x1 << " X2: " << x2 << endl;
                                    cout << "CA: " << str.substr(lf,x2-x1+1) << " " << str.substr(x1, x2-x1+1) << endl;*/
                                    if (CheckAna(str, lf, x1, x2-x1+1))
                                        uaps++;
//                                    cout << "updated uaps: " << uaps << endl;
                                }
                            }
                        }
                    }
                }
            }
        }
        cout << uaps << endl;
    }       //End for total = 0 T-1
    
    return 0;
}
