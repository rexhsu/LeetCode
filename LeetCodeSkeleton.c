/* 
 * For debug purpose, compiler with -DDEBUG
 */

#ifdef DEBUG
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef int bool;

#define true 1
#define false 0
#endif

/*
 * Solution context start
 */

/*
 * Solution context end 
 * Try to call your functions in main()
 */

#ifdef DEBUG
int main(void) {
    printf("LeetCode debug version for %s\n", __FILE__);
    return 0;
}
#endif

