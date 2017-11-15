// The following program computes
//the probability for dice possibilities
#include  <iostream>   //drops .h still available
#include <random>
using namespace std;
const int sides = 6; //replaces many sharp defines
int main()
{
    const int n_dice = 2;
    uniform_int_distribution<unsigned> u(1,6);
    default_random_engine e(time(0));

    cout << "\nEnter number of trials: ";
    int trials;
    cin >> trials;  //compare to scanf

    vector<int> outcomes(n_dice * sides +1);
    for (int j = 0; j < trials; ++j)
        outcomes[u(e) + u(e)]++;

    cout << "probability\n";
    double sum = 0;
    for (int j = 2; j < n_dice * sides + 1; ++j) {
        int num = outcomes[j];
        double p = static_cast<double>(num) / trials;
        sum = sum + p;
        cout << "j = " << j << " num_successes = " << num << " p = "
             << p
             << endl;
    }
    cout << "sum p = " << sum << endl;
}

