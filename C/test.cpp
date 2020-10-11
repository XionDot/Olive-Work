#include <iostream>
using namespace std;

int main()
{
    cout <<"Enter num:";
    int num;
    cin >> num;
    int nums[num], sum = 0;
    cout << "Enter N numbers: \n";

    for (int i = 0; i < num; ++i)
    {
        cin >> nums[i];
        sum += nums[i];
    }
    
    cout << "Sum = " << sum << endl;

    return 0;
}
