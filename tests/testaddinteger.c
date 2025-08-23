#include "unity.h"
#include "embeddedlib.h"

void setUp(void) {}
void tearDown(void) {}

void test_add_integer_basic(void) {
    int result;
    TEST_ASSERT_EQUAL(5, elib_addinteger(2, 3));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add_integer_basic);
    return UNITY_END();
}