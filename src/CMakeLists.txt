add_library(EmbeddedLib STATIC embeddedlib.c)

target_include_directories(EmbeddedLib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)