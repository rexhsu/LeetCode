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
} *lruHead = NULL, *lruTail = NULL, *table;

int cap;
int curSiz;

void lruCacheInit(int capacity) {
    cap = capacity;
    curSiz = 0;
    table = calloc(10240, sizeof(struct lruEnt));
}

void lruCacheFree() {
    free(table);
}

void assEnt(struct lruEnt *ent, int key, int val) {
    ent->key = key;
    ent->val = val;
}

void mvEntAhead(struct lruEnt *ent) {
    if (ent == lruHead) return;
    if (cap == 1) {
        lruHead = ent;
        return;
    }
    /* move out first */
    if (ent->pre)
        ent->pre->nxt = ent->nxt;
    if (ent->nxt)
        ent->nxt->pre = ent->pre;
    /* put ahead */
    lruHead->pre = ent;
    ent->nxt = lruHead;
    ent->pre = NULL;
    lruHead = ent;
}

void rmTailEnt() {
    lruTail->val = 0;
    lruTail = lruTail->pre;
    lruTail->nxt = NULL;
}

int lruCacheGet(int key) {
    struct lruEnt *ent = lruHead;
    if (table[key].val) return table[key].val;
    return -1;
}

void lruCacheSet(int key, int value) {
    struct lruEnt *ent;
    if (!lruHead) {             // first item
        table[key].val = value;
        lruHead = &table[key];
        lruTail = &table[key];
        curSiz = 1;
    }
    printf("set table[%d].val = %d\n", key, table[key].val);
    if (!table[key].val) {          // not found
        if (curSiz < cap) {         // allocate empty
            ent = &table[key];
            assEnt(ent, key, value);
            mvEntAhead(ent);
            curSiz++;
        } else {                    // remove existed one
            ent = &table[key];
            assEnt(ent, key, value);
            if (curSiz > 1) rmTailEnt();
            mvEntAhead(ent);
        }
    } else {                        // found
        ent = &table[key];
        assEnt(ent, key, value);
        if (curSiz > 1 && ent == lruTail)
            lruTail = ent->pre;
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
    lruCacheSet(2, 2);
    lruCacheList("after set (2, 2)");
    lruCacheGet(2);
    lruCacheList("after get (2)");
    lruCacheSet(1, 1);
    lruCacheList("after set (1, 1)");
    lruCacheSet(4, 1);
    lruCacheList("after set (4, 1)");
    lruCacheGet(2);
    lruCacheList("after get (2)");

    return 0;
}
#endif

