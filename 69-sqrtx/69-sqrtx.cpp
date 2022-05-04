class Solution {
public:
    int mySqrt(int x) {
        int s = bsrch(0, x, x);
        if (s*s <= x) return s;
        else return s-1;
    }
    int bsrch(int l, int r, int x) {
        //cout << l << " " << r << endl;
        if (r>46340) r=46340;
        if (l>=r) return l;
        else {
            int mid = (l+r)/2;
            int v = mid*mid;
            if (v>x) return bsrch(l, mid-1, x);
            else if (v<x) return bsrch(mid+1, r, x);
            else return mid;
        }
    }
};