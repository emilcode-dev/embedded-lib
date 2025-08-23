add_library(embeddedlib STATIC embeddedlib.c)

target_include_directories(embeddedlib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)