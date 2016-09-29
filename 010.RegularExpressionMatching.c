int slen, plen, plenm1;
bool tryMatch(char *s, int sidx, char *p, int pidx) {
    if (pidx == plen) return sidx == slen;
    if ((pidx < plenm1 && p[pidx+1] != '*') || pidx == plenm1)
        return (sidx < slen && (s[sidx] == p[pidx] || p[pidx] == '.')) && tryMatch(s, sidx+1, p, pidx+1);
    while (s[sidx] == p[pidx] || p[pidx] == '.') {
        if (tryMatch(s, sidx, p, pidx+2)) return true;
        if (++sidx >= slen) break;
    }
    return tryMatch(s, sidx, p, pidx+2);
}

bool isMatch(char* s, char* p) {
    slen = strlen(s);
    plen = strlen(p);
    plenm1 = plen - 1;
    return tryMatch(s, 0, p, 0);
}
