#include <iostream>
using namespace std;

int main()
{
    int N, l_sum = 0, r_sum = 0;
    cin >> N;
    int a[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
        cin >> a[i][j];
        if (i == j)
        {
            l_sum += a[i][j];
        }
    }
}
for (int i = 0; i < N; i++)
{
    for (int j = N-1-i; j >= 0;)
    {
        r_sum += a[i][j];
        break;
    }
}
cout << abs(l_sum - r_sum) << endl;
return 0;
}
