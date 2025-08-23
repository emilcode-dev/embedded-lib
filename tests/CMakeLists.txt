add_executable(TestAddInteger testaddinteger.c)

target_include_directories(TestAddInteger PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)

target_link_libraries(TestAddInteger PRIVATE embeddedlib unity)

add_test(NAME UnittestAddInteger COMMAND TestAddInteger)