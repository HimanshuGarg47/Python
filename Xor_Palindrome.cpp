#include <iostream>
#include <string>   
using namespace std;

int main()
{
    int t, n;
    cin >> t;
    while (t--)
    {

        cin >> n;
        string str;
        cin >> str;

        if(n & 1)
        cout << "YES" << endl;
        else
        {
            int zero = 0, one = 0;
            for(int i = 0;i<n;i++)
            {
                if(str[i] == '0')
                zero++;
                else
                one++;
            }
            if(zero == 0 || one == 0 || zero==one || one%2==0)
            cout << "YES" << endl;
            else
            cout << "NO" << endl;
           
            
        }

    }
}