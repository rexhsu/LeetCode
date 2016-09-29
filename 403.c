/*
 * Initially, the frog is on the first stone and assume the first jump must be 1 unit.
 * If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units forward.
 * The number of stones is ≥ 2 and is < 1,100.
 * Each stone's position will be a non-negative integer < 2^31.
 * The first stone's position is always 0.
 */

#define RS 1100
#define CS 1100
char dp_tab[RS][CS];
int stones_arr[RS];
int stones_siz;

int stoneIndex(int cur, int step) {
    for (--step; step < stones_siz; step++)
        if (stones_arr[step] == cur) return step;
    return 0; 
}

bool isStone(int cur, int step) {
    for (step; step < stones_siz; step++)
        if (stones_arr[step] == cur) return true;
    return false;
}

bool tryCross(int cur, int k, int step) {
    bool ret = false;
    int nxt = cur + k;
    int curIdx = stoneIndex(cur, step), nxtIdx = stoneIndex(nxt, step);

    if (curIdx == stones_siz - 1) return false;
    if (stones_arr[curIdx+1] - cur > k + 1) return false;

    if (dp_tab[nxtIdx][curIdx] == 1) return true;
    else if (dp_tab[nxtIdx][curIdx] == -1) return false;

    if (!isStone(cur, step) || !k || ++step == stones_siz) return false;
    if (nxt == stones_arr[stones_siz-1]) return true;
 
    ret = tryCross(nxt, k, step) || tryCross(nxt, k-1, step) || tryCross(nxt, k+1, step);

    if (ret)
        dp_tab[nxtIdx][curIdx] = 1;
    else
        dp_tab[nxtIdx][curIdx] = -1;

    return ret;
}

void fill_stones_arr(int *stones) {
    int i; 
    for (i = 0; i < stones_siz; i++) stones_arr[i] = stones[i];
}

bool canCross(int* stones, int stonesSize) {
    int i;
    if (stones[1] != 1) return false;
    if (stonesSize == 2) return true;
    stones_siz = stonesSize;
    for (i=0; i<stonesSize; i++)
        memset(dp_tab[i], 0, stonesSize);
    fill_stones_arr(stones);
    return tryCross(1, 1, 1) || tryCross(1, 2, 1);
}
