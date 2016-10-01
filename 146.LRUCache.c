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
#ifndef DEBUG
#define printf()
#endif

int cap;
int *lruKtab;
int *lruVtab;
int *lruTtab;

void lruCacheInit(int capacity) {
    cap = capacity;
    lruKtab = calloc(cap, 4);
    lruVtab = calloc(cap, 4);
    lruTtab = calloc(cap, 4);
}

void lruCacheFree() {
    free(lruKtab);
    free(lruVtab);
    free(lruTtab);
}

int lruCacheGet(int key) {
    int i=0, j=-1;
    for (;i<cap;i++) {
        if (lruTtab[i]) {
            if (lruKtab[i] == key) {
                j = lruVtab[i];
                lruTtab[i] = 1;
            }
            else lruTtab[i]++;
        }
    }
    printf("lruCacheGet(%d) return %d\n", key, j);
    return j;
}

void lruCacheSet(int key, int value) {
    int i, empty = -1, found = 0, maxt = 0, maxti = -1;
    printf("start to set (%d,%d)\n", key, value);
    for (i=0; i<cap; i++) {
        if (!lruTtab[i]) {
            printf("empty Ttab[%d]=%d, maxti=%d\n", i, lruTtab[i], maxti);
            if (empty == -1) empty = i;
        }
        else if (lruKtab[i] == key) {
            printf("key found\n");
            lruVtab[i] = value;
            lruTtab[i] = 1;
            found = 1;
        }
        else {
            if (lruTtab[i] > maxt) {
                maxt = lruTtab[i];
                maxti = i;
            }
            printf("Ttab[%d]=%d, maxti=%d\n", i, lruTtab[i], maxti);
            lruTtab[i]++;
        }

    }
    printf("found %d empty %d maxti %d\n", found, empty, maxti);
    if (!found && empty != -1) {
        lruKtab[empty] = key;
        lruVtab[empty] = value;
        lruTtab[empty] = 1;
        found = 1;
    }
    if (!found && maxti > -1) {
        lruKtab[maxti] = key;
        lruVtab[maxti] = value;
        lruTtab[maxti] = 1;
    }
}

/*
 * Solution context end 
 * Try to call your functions in main()
 */

#ifdef DEBUG
void lruCacheList(char *s) {
    int i=0, j=-1;
    printf("%s\n     Key    Value     Time cap:%d\n", s, cap);
    for (;i<cap;i++) {
        printf("%8d %8d %8d\n", lruKtab[i], lruVtab[i], lruTtab[i]);
    }
}

int main(void) {
    printf("LeetCode debug version for %s\n", __FILE__);

    lruCacheInit(2);
    lruCacheSet(2, 1);
    lruCacheSet(2, 2);
    lruCacheList("after set (2, 1) (2, 2)\n");
    lruCacheGet(2);
    lruCacheList("after get (2)\n");
    lruCacheSet(1, 1);
    lruCacheSet(4, 1);
    lruCacheList("after set (1, 1) (4,1)\n");
    lruCacheGet(2);

    return 0;
}
#endif

