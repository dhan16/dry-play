#include <iostream>
#include <boost/thread.hpp>
#include <boost/chrono.hpp>

void wait(int seconds)
{
    boost::this_thread::sleep_for(boost::chrono::seconds{seconds});
}

void thread()
{
    for (int i = 0; i < 5; ++i)
    {
        wait(1);
        std::cout << i << '\n';
    }
}

void boost_thread_main()
{
    std::cout << "Running thread_main" << std::endl;
    boost::thread t{thread};
    t.join();
}
