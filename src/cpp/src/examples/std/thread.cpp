#include <iostream>
#include <thread>
#include <sstream>

inline void msg(const std::string &s)
{
    std::stringstream stream;
    stream << std::this_thread::get_id() << "  message is = " << s << std::endl;
    std::cout << stream.str();
}

void thread_function1(const std::string &s)
{
    msg(s);
}

void thread_function2(std::string &s)
{
    msg(s);
    s = "Justin Beaver";
}

int std_thread_main()
{
    std::cout << "Number of threads = "
              <<  std::thread::hardware_concurrency() << std::endl;

    std::string s = "Kathy Perry";
    std::thread t2(&thread_function2, std::ref(s));
    std::thread t1(&thread_function1, s);

    msg(s);
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    msg(s);

    t1.join();
    t2.join();
    return 0;
}
