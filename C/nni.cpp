#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b;
    int z;
    cin >> a >> b;

    if (a > b) {

        z = a - b;
        cout << z;
    }
    else {
        z = b - a;
        cout << z;
    }
}
