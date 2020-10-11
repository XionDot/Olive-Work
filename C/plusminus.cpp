#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int i, j, c0 = 0, c1 = 0, c2 = 0;
	int arr[500];
	float n;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
		if(arr[i]<0)
			c1++;
		else if(arr[i]>0)
			c2++;
		else
			c0++;
	}
	cout << c1/n << endl;
    cout << c2/n << endl;
    cout << c0/n << endl;
}
