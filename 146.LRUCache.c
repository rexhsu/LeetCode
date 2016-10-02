#ifndef DEBUG
#define printf()
#endif

struct lruEnt {
    int key;
    int val;
    struct lruEnt *pre;
    struct lruEnt *nxt;
} *lruHead = NULL, *lruTail = NULL, *table = NULL;

int cap;
int curSiz;

void lruCacheInit(int capacity) {
    int i = 0;
    cap = capacity;
    curSiz = 0;
    table = calloc(10240, sizeof(struct lruEnt));
    lruHead = NULL;
    lruTail = NULL;
}

void lruCacheFree() {
    free(table);
}

void assEnt(struct lruEnt *ent, int key, int val) {
    ent->key = key;
    ent->val = val;
}

#define OPR ((op>679 && op<681))

void mvEntAhead(struct lruEnt *ent) {
    if (ent == lruHead) return;
    if (cap == 1) {
        lruHead = ent;
        lruTail = ent;
        return;
    }

    /* move out first */
    if (ent->pre) {
        if (ent == lruTail) lruTail = ent->pre;
        ent->pre->nxt = ent->nxt;
    }
    if (ent->nxt)  ent->nxt->pre = ent->pre;
    /* put ahead */
    lruHead->pre = ent;
    ent->nxt = lruHead;
    ent->pre = NULL;
    lruHead = ent;
}

void rmTailEnt() {
    struct lruEnt *ent;
    ent = lruTail;
    lruTail->val = 0;
    if (lruTail->pre) lruTail = lruTail->pre;
    lruTail->nxt = NULL;
    ent->pre = NULL;
    ent->nxt = NULL;
}

int lruCacheGet(int key) {
    struct lruEnt *ent;
    if (table[key].val) {
        ent = &table[key];
        if (curSiz > 1 && ent == lruTail)
            lruTail = ent->pre;
        mvEntAhead(ent);
        return table[key].val;
    }
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
    if (table[key].val == 0) {      // not found
        if (curSiz < cap) {         // allocate empty
            ent = &table[key];
            assEnt(ent, key, value);
            mvEntAhead(ent);
            curSiz++;
        } else {                    // replace existed one
            rmTailEnt();
            ent = &table[key];
            assEnt(ent, key, value);
            mvEntAhead(ent);
        }
    } else {                        // found
        ent = &table[key];
        assEnt(ent, key, value);
        mvEntAhead(ent);
    }
}

