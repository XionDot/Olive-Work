#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    int h, w;

    scanf("%d", &n);
    for (w = 1; w <= n; ++w)
    {
        for (h = 1; h <= n; ++h)
        {
            if (h <= (n - w))
                printf(" ");
            else
                printf("#");
        }
        printf("\n");
    }
return 0;
}
