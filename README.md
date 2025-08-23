# Generic Embedded Software Library

* run docker
* run dev container in vs code
* build project
    mkdir build && cd build
    - test:
        cmake -DTARGET_GROUP=test .. 
        cmake --build .
        ctest
    - production:
        cmake -DTARGET_GROUP=production ..
        cmake --build .