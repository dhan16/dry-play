#include <boost/lambda/lambda.hpp>
#include <iostream>

void boost_lambda_main()
{
    using namespace boost::lambda;
    typedef std::istream_iterator<float> in;

    std::cout << "Type in any number: ";

    int mul = 4;
    std::find_if(in(std::cin), in(), [&mul](float a)
    {
        std::cout << a * mul << "\nType in another number: ";
        return a<0;
    });

    std::for_each(
            in(std::cin), in(), std::cout << (_1 * 3) << "\nType in another number: " );
}
