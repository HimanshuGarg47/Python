#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        vector<int> arr;
        int temp;
        for (int i = 1; i <= n; i++)
        {
            cin >> temp;
            arr.push_back(temp);
        }

        int j = 1, i = 0;
        int count = 0;
        while (i < n)
        {
            if (j == arr[i])
            {
                count++;
                j += 1;
            }
            else
            {
                i++;
                j++;
            }
        }
        cout << count << endl;
    }
}