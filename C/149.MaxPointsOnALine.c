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
    for (; cp; cp = cp->nxt) if (cp->x == x && cp->y == y) return cp;
    return NULL;
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
    for (; line; line = line->nxt) if (line->dx == dx && line->dy == dy && line->dxb == dxb) return line;
    return NULL;
}

bool cponline(struct CntPoint *cp, struct Line *line) {
    return (line->dx * cp->y == line->dy * cp->x + line->dxb);
}

int maxPoints(struct Point* points, int pointsSize) {
    int i=0, j, x1, y1, x2, y2, max=0, dx, dy, dxb, cnt;
    struct CntPoint* cp;
    struct Line *line;
    
    cphead = NULL;
    lhead = NULL;
    
    if (pointsSize == 1 || pointsSize == 2) return pointsSize;
    for (; i<pointsSize; i++) {
        x1 = points[i].x;
        y1 = points[i].y;
        if ((cp = getCntPoint(x1, y1))) {
            cp->cnt++;
            continue;
        } else {
            cp = (struct CntPoint *)malloc(sizeof(struct CntPoint));
            cp->x = x1;
            cp->y = y1;
            cp->cnt = 1;
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
                line = (struct Line *)malloc(sizeof(struct Line));
                line->dx = dx;
                line->dy = dy;
                line->dxb = dxb;
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

    while (line) {
        cnt = 0;
        cp = cphead;
        while (cp) {
            if (cponline(cp, line)) cnt += cp->cnt;
            cp = cp->nxt;
        }
        if (cnt > max) max = cnt;
        if (max == pointsSize) return max;
        line = line->nxt;
    }
    return max;
}
