#define LEETCODE

#ifndef LEETCODE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef int bool;

#define true 1
#define false 0

/**
 * Definition for a point.
 */
struct Point {
     int x;
     int y;
};
#else
#define printf()
#endif

 
 /**
  * Definition for a cnt point.
  */
struct CntPoint {
    int x;
    int y;
    int cnt;
    struct CntPoint *nxt;
} *cphead;

struct CntPoint* getCntPoint(int x, int y) {
    struct CntPoint *cp = cphead;
    printf("getCntPoint(%d, %d)\n", x, y);
    for (; cp; cp = cp->nxt) if (cp->x == x && cp->y == y) return cp;
    return cp;
}

void setCntPoint(struct CntPoint* cp, int x, int y, int cnt) {
    cp->x = x;
    cp->y = y;
    cp->cnt = cnt;
}

 /**
  * Definition for a line.
  * y = ax + b 
  * a = dy/dx
  * dx * y = dy * x + dx * b
  */
struct Line {
    int dx;
    int dy;
    int dxb;
    struct Line *nxt;
} *lhead;
 
struct Line* getLine(int dx, int dy, int dxb) {
    struct Line *line = lhead;
    printf("getLine(%d, %d, %d)\n", dx, dx, dxb);
    while (line) {
        if (line->dx == dx && line->dy == dy && line->dxb == dxb) return line;
        line = line->nxt;
    }
    return NULL;
}

void setLine(struct Line* line, int dx, int dy, int dxb) {
    line->dx = dx;
    line->dy = dy;
    line->dxb = dxb;
}

#define SMAX 10000
#define PRECISION 10
#define MAX( x, y ) ( ((x) > (y)) ? (x) : (y) ) 
#define MIN( x, y ) ( ((x) < (y)) ? (x) : (y) ) 

bool cponline(struct CntPoint *cp, struct Line *line) {
    //  dx * y = dy * x + dx * b
    printf("  dx*y %d dy*x %d dx*b %d\n", (line->dx * cp->y),
        (line->dy * cp->x), line->dxb);
    return (line->dx * cp->y == line->dy * cp->x + line->dxb);
}

float slope(int x1, int y1, int x2, int y2) {
    printf("slope (%d, %d) and (%d, %d) is %f\n", x1, y1, x2, y2, (float)(y1-y2)/(x1-x2));
    if (x1 == x2) return -SMAX;
    return (float)(y1-y2)/(x1-x2);
}

int maxPoints(struct Point* points, int pointsSize) {
    int i=0, j, x1, y1, x2, y2, max, dx, dy, dxb, cnt;
    float a, b;
    struct CntPoint* cp;
    struct Line *line;
    
    cphead = NULL;
    lhead = NULL;
    
    if (pointsSize == 1) return 1;
    for (; i<pointsSize; i++) {
        x1 = points[i].x;
        y1 = points[i].y;
        if ((cp = getCntPoint(x1, y1))) {
            cp->cnt++;
            continue;
        } else {
            printf("allocate new cp\n");
            cp = (struct CntPoint *)malloc(sizeof(struct CntPoint));
            setCntPoint(cp, x1, y1, 1);
            if (!cphead) {
                cphead = cp;
                cp->nxt = NULL;
            } else {
                cp->nxt = cphead->nxt;
                cphead->nxt = cp;
            }
        }
        for (j=i+1; j<pointsSize; j++) {
            x2 = points[j].x;
            y2 = points[j].y;
            dx = x1 - x2;
            dy = y1 - y2;
            if (!dx && !dy) continue;
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            }
            dxb = dx*y1 - dy*x1;
            line = getLine(dx, dy, dxb);
            if (!line) {
                printf("allocate new line\n");
                line = (struct Line *)malloc(sizeof(struct Line));
                setLine(line, dx, dy, dxb);
                if (!lhead) {
                    lhead = line;
                    line->nxt = NULL;
                } else {
                    line->nxt = lhead->nxt;
                    lhead->nxt = line;
                }
            }
        }
    }
    line = lhead;
    if(!line && cphead) return cphead->cnt;
    i=0; 
    j=0;
    max = 0;
    while (line) {
        cnt = 0;
        printf("verify line (%d, %d, %d)\n", line->dx, line->dy, line->dxb);
        cp = cphead;
        while (cp) {
            if (cponline(cp, line)) {
                printf("  cp %d(%d, %d) online\n", cp->cnt, cp->x, cp->y);
                cnt += cp->cnt;
                //i++;
                //printf("i %d\n", i);
            } else printf("  cp %d(%d, %d) outline\n", cp->cnt, cp->x, cp->y);
            cp = cp->nxt;
        }
        if (cnt > max) max = cnt;
        line = line->nxt;
        //j++;
        //printf("j %d\n", j);
    }
    return max;
}

#ifndef LEETCODE
int main() {
    struct Point pa[9]; 
    pa[0].x = 84;
    pa[0].y = 250;
    pa[1].x = 0;
    pa[1].y = 0;
    pa[2].x = 1;
    pa[2].y = 0;
    pa[3].x = 0;
    pa[3].y = -70;
    pa[4].x = 0;
    pa[4].y = -70;
    pa[5].x = 1;
    pa[5].y = -1;
    pa[6].x = 21;
    pa[6].y = 10;
    pa[7].x = 42;
    pa[7].y = 90;
    pa[8].x = -42;
    pa[8].y = -230;
    printf("start to call maxPoints\n");
    printf("maxPoints return %d\n", maxPoints(pa, 9));
    return 0;
}
#endif

