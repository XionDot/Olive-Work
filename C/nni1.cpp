#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int intArr[n];
    for (int i = 0; i < n; i++){
    //Now we call the sort function
    cin>>intArr[i];
    }
    sort(intArr, intArr + n);
    
    cout << "Sorted Array looks like this." << endl;
    for (size_t i = 0; i != n; ++i)
        cout << intArr[i] << " ";

    return 0;
}

