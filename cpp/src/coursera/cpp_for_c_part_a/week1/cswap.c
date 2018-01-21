#include <printf.h>

void swap_int(int* i, int* j)
{
    int temp = *i;
    *i = *j;
    *j = temp;
}

void swap_double(double* i, double* j)
{
    double temp = *i;
    *i = *j;
    *j = temp;
}

int main() {
    int i=5, j=10;
    printf("inputs:%d %d\n", i, j);
    swap_int(&i, &j);
    printf("outputs:%d %d\n", i, j);

    double x=5.3, y=10.6;
    printf("inputs:%1f %1f\n", x, y);
    swap_double(&x, &y);
    printf("outputs:%1f %1f\n", x, y);
}



