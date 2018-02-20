/*
The median of a dataset of integers is the midpoint value of the dataset for which an equal number of integers are less than and greater than the value.
To find the median, you must first sort your dataset of integers in non-decreasing order, then:

    If your dataset contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted dataset {1,2,3} , 2 is the median.
    If your dataset contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted dataset {1,2,3,4} , (2+3)/2=2.5 is the median.

Given an input stream of n integers, you must perform the following task for each ith integer:

    Add the ith integer to a running list of integers.
    Find the median of the updated list (i.e., for the first element through the ith element).
    Print the list's updated median on a new line. The printed value must be a double-precision number scaled to decimal place (i.e.,12.3 format).

*/

#include<iostream>
#include<vector>
#include<iomanip>
using namespace std;

void getMedian(vector<int> a)
{
  int vectorSize = a.size(),count = 1;
  float median = 0.0;
  median = a[0];
  printf("%.1f\n",median);
  for(int i=1;i<vectorSize;i++)
  {
    int j=i-1,key = a[i];
    while(j>=0 and a[j]>key)
    {
      a[j+1] = a[j];
      j--;
    }
    a[j+1] = key;
    count +=1;
    int mid = count/2;
    if(count%2==0)
    {
      median = (a[mid] + a[mid-1])/2.0;
    }
    else
    {
      median = a[mid];
    }
    printf("%.1f\n",median);
  }
}

int main()
{
  int n;
  cin>>n;
  vector<int> a(n);
  for(int a_i=0;a_i<n;a_i++) cin>>a[a_i];
  getMedian(a);
  return 0;
}
