#include <iostream>
using namespace std;
template <class T1, class T2>
void generic_copy(const T1 src[], T2 dest[], int size)
{
    for (int i = 0; i < size; ++i)
        dest[i] = static_cast<T2>(src[i]);
};

template <class T>
void printArr(const T a[], int size, const string &name="arr")
{
    cout << name << ":";
    for (int i = 0; i < size; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;
};


int main()
{
    const int size =5;
    auto * srci = new int[size]{0, 5};
    auto * dsti = new int[size];
    printArr(srci, size, "srci");
    generic_copy(srci, dsti, size);
    printArr(dsti, size, "dsti");

    auto * srcd = new double[size]{1.1, -7.1};
    auto * dstd = new double[size];
    printArr(srcd, size, "srcd");
    generic_copy(srcd, dstd, size);
    printArr(dstd, size, "dstd");

    generic_copy(srci, dstd, size);
    printArr(dstd, size, "dstd");

    generic_copy(srcd, dsti, size);
    printArr(dsti, size, "dsti");

//    auto * dsts = new string[size];
//    printArr(dsts, size, "dsts");
//    generic_copy(srcd, dsts, size);
//    printArr(dsts, size, "dsts");
}
