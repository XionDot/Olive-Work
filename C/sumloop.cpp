//#include<bits/stdc++.h>

#include <iostream>
using namespace std;

int main (){
	int n, sum =0;
	cout << "Enter Numbers\n";
	
	for  (int i =0; i<45; i++){
		cin >> n;
		sum += n;
	}
	cout << "sum is: \n" << sum;
	return 0;
}
