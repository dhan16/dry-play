/* Convert this program to C++
* change to C++ io
* change to one line comments
* change defines of constants to const
* change array to vector<>
* inline any short function
*/

#include <iostream>
#include <vector>

using namespace std;

const int N=40;

inline void sum(int &s, int size, const int d[])
{
    for(int i = 0; i < size; ++i)
        s += d[i];
}

int main()
{
    vector<int> data(N);
    for(int i = 0; i < N; ++i)
        data[i] = i;

    int accum = 0;
    sum(accum, data.size(), &data[0]);
    cout << "sum is " << accum << endl;
    cout << "sum is " << N * (N - 1) / 2 << endl;
    return 0;
}
