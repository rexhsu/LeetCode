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

struct lruEnt {
    int key;
    int val;
    struct lruEnt *pre;
    struct lruEnt *nxt;
} *lruHead;

void lruCacheInit(int capacity) {
    int i;
    lruHead = calloc(capacity, sizeof(struct lruEnt));
    for (i=1; i<capacity; i++)
        lruHead[i].pre = &lruHead[i-1];
    for (i=0; i<capacity-1; i++)
        lruHead[i].nxt = &lruHead[i+1];
    lruHead[0].pre = NULL;
    lruHead[capacity-1].nxt = NULL;
}

void lruCacheFree() {
    free(lruHead);
}

void mvEntAhead(struct lruEnt *ent) {
    if (ent == lruHead) return;
    /* move out first */
    ent->pre->nxt = ent->nxt;
    if (ent->nxt)
        ent->nxt->pre = ent->pre;
    /* put ahead */
    lruHead->pre = ent;
    ent->nxt = lruHead;
    ent->pre = NULL;
    lruHead = ent;
}

int lruCacheGet(int key) {
    struct lruEnt *ent = lruHead;
    while(ent->key) {
        if (ent->key == key) {
            mvEntAhead(ent);
            return ent->val;
        }
        if (ent->nxt) ent = ent->nxt;
        else break;
    }
    
    printf("lruCacheGet(%d) return -1\n", key);
    return -1;
}

void lruCacheSet(int key, int value) {
    struct lruEnt *ent = lruHead;
    while(ent->key) {
        if (ent->key == key) {
            ent->val = value;
            mvEntAhead(ent);
            return;
        }
        if (ent->nxt) ent = ent->nxt;
        else break;
    }
    if (!ent->key || !ent->nxt) {
        ent->key = key;
        ent->val = value;
        mvEntAhead(ent); 
    }
}

/*
 * Solution context end 
 * Try to call your functions in main()
 */

#ifdef DEBUG
void lruCacheList(char *s) {
    struct lruEnt *ent = lruHead;
    printf("%s:\n", s);
    while(true) {
        printf("(%d, %d) nxt %p ", ent->key, ent->val, ent->nxt); 
        if (ent->nxt) ent = ent->nxt;
        else break;
    }
    printf("\n");
}

int main(void) {
    printf("LeetCode debug version for %s\n", __FILE__);

    lruCacheInit(2);
    printf("init ok\n");
    lruCacheSet(2, 1);
    lruCacheList("after set (2, 1)");
    lruCacheSet(3, 2);
    lruCacheList("after set (3, 2)");
    lruCacheGet(3);
    lruCacheGet(2);
    lruCacheList("after get (2)");
    lruCacheSet(4, 3);
    lruCacheList("after set (4, 3)");
    lruCacheGet(2);
    lruCacheGet(3);
    lruCacheGet(4);

    return 0;
}
#endif

