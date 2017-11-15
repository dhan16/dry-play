#include <iostream>
using namespace std;

inline void swap1(int& i, int& j)
{
    int temp = i;
    i = j;
    j = temp;
}

inline void swap1(double& i, double& j)
{
    double temp = i;
    i = j;
    j = temp;
}

int main() {
    int i=5, j=10;
    double x=5.3, y=10.6;

    cout << "inputs:" << i << j <<endl;
    swap1(i, j);
    cout << "outputs:" << i << j <<endl;

    cout << "inputs:" << x << y <<endl;
    swap1(x, y);
    cout << "outputs:" << x << y <<endl;
}
