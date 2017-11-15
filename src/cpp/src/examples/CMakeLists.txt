cmake_minimum_required(VERSION 3.8)
project(examples)
set(CMAKE_CXX_STANDARD 11)

link_directories(/usr/local/lib)

include_directories(include)
include_directories(boost/include)
include_directories(std/include)

set(SOURCE_FILES
        boost/lambda.cpp
        boost/regex.cpp
        boost/noncopyable.cpp
        boost/stringref.cpp
        boost/thread.cpp
        boost/binary.cpp
        boost/shared_memory.cpp
        std/thread.cpp
        std/initializer_list.cpp
        graphics/raytracing_spheres.cpp)

add_executable(runexample runexample.cpp ${SOURCE_FILES})
target_link_libraries(runexample boost_regex boost_system boost_thread-mt)