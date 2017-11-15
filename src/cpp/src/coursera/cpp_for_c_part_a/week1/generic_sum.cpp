#include <iostream>
#include <complex>

using namespace std;

template <class T>
T sum(const T data[], int size, T s=0)
{
    for (int i = 0; i < size; ++i)
        s += data[i];
    return s;
}

int main() {
    int size = 10;
    auto * a = new int[size];
    auto * d = new double[size];
    auto * c = new complex<double>[size];
    for (int j = 0; j < size; ++j)
    {
        a[j] = j*2;
        d[j] = j*1.5;
        c[j] = complex<double>(a[j], d[j]);
    }

    cout << "suma:" << sum(a, size) <<endl;
    cout << "sumd:" << sum(d, size) <<endl;
    cout << "sumc:" << sum(c, size) <<endl;
}