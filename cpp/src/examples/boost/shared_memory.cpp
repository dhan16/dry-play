#include <boost/interprocess/shared_memory_object.hpp>
#include <boost/interprocess/mapped_region.hpp>
#include <iostream>

using namespace boost::interprocess;

void boost_shared_memory_main()
{
    // create
    shared_memory_object shdmem{open_or_create, "Boost", read_write};
    shdmem.truncate(1024);
    std::cout << shdmem.get_name() << '\n';
    offset_t size;
    if (shdmem.get_size(size))
        std::cout << size << '\n';

    // region1
    mapped_region region{shdmem, read_write};
    std::cout << std::hex << region.get_address() << '\n';
    std::cout << std::dec << region.get_size() << '\n';
    auto *i1 = static_cast<int*>(region.get_address());
    *i1 = 99;

    // region2
    mapped_region region2{shdmem, read_only};
    std::cout << std::hex << region2.get_address() << '\n';
    std::cout << std::dec << region2.get_size() << '\n';
    auto *i2 = static_cast<int*>(region2.get_address());
    std::cout << *i2 << '\n';

    bool removed = shdmem.remove("Boost");
    std::cout << "Remove returned with " << removed << std::endl;
}