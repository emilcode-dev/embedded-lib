#include "embeddedlib/embeddedlib.h"
#include <stdint.h>

int main() {
    int32_t sum;
    int32_t a = 5;
    int32_t b = 10;
    sum = elib_addinteger(a, b);
}