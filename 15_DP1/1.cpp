// https://www.acmicpc.net/problem/1003
//피보나치 함수

#include <iostream>
using namespace std;
long long fibArray[41] = {0,1,};

int fib(int n)
{
    int i = 0;
    for (i = 2; i <= n; i++)
    {
        fibArray[i] = fibArray[i - 1] + fibArray[i - 2];
    }

    return fibArray[n];
}

int main()
{

    int t, n;
    cin >> t;

    for (int i = 0; i < t; i++)
    {

        cin >> n;
        if (n == 0)
        {
            cout << "1 0" << '\n';
        }
        else
        {
            fib(n);
            cout << fibArray[n-1] << ' ' << fibArray[n] << '\n';
        }
    }

    return 0;
}