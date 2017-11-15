#include <iostream>
#include <complex>

using namespace std;

template <class T>
inline void swap2(T& i, T& j)
{
    T temp = i;
    i = j;
    j = temp;
}

int main() {
    int i=5, j=10;
    double x=5.3, y=10.6;
    complex<double> r(1, 2.0), s(3.0, 4);

    cout << "inputs:" << i << j <<endl;
    swap2(i, j);
    cout << "outputs:" << i << j <<endl;

    cout << "inputs:" << x << y <<endl;
    swap2(x, y);
    cout << "outputs:" << x << y <<endl;

    cout << "inputs:" << r << s <<endl;
    swap2(r, s);
    cout << "outputs:" << r << s <<endl;
}

