#include <iostream>
#include <sstream>
#include <vector>
#include "examples.h"

using namespace std;

typedef void (*Func)();
struct ExampleStruc {
    std::string name;
    Func fn;
};

static vector<ExampleStruc> choices = {
        // std
        {"std_thread_main", [] { std_thread_main(); } },
        {"std_initializer_list_main", [] { std_initializer_list_main(); } },
        // boost
        {"boost_binary_main", [] { boost_binary_main(); } },
        {"boost_thread_main", [] { boost_thread_main(); } },
        {"boost_noncopyable_main", [] { boost_noncopyable_main(); } },
        {"boost_stringref_main", [] { boost_stringref_main(); } },
        {"boost_lambda_main", [] { boost_lambda_main(); } },
        {"boost_regex_main", [] { boost_regex_main(); } },
        {"boost_shared_memory_main", [] { boost_shared_memory_main(); } },
        // others
        {"raytracing_spheres_main", [] { raytracing_spheres_main(); } },
};

std::string makeMenu(const vector<ExampleStruc> &pStruct) {
    std::stringstream stream;
    stream << "Menu:" << endl;
    for (int index = 0; index < pStruct.size(); ++index)
    {
        auto s = pStruct[index];
        stream << index << ":" << s.name << endl;
    }
    return stream.str();
}

int main()
{
    std::string menuChoices = makeMenu(choices);
    while(true)
    {
        std::cout << menuChoices;
        cout << "Enter choice(-1 to exit):\n" << endl;
        int index;
        cin >> index;  //compare to scanf

        if(index < 0)
            break;
        auto s = choices[index];
        cout << "Running " << s.name << endl;
        s.fn();
        cout << "Finished " << s.name << endl;
    }
}

