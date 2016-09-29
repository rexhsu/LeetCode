int slen, plen, plenm1;
bool tryMatch(char *s, int sidx, char *p, int pidx) {
    if (pidx == plen) return sidx == slen;
    if (pidx == plenm1)
        if (sidx == slen - 1 && (s[sidx] == p[pidx] || p[pidx] == '.')) return true;
        else return false;
    if (pidx < plenm1 && p[pidx+1] != '*')
        if (sidx < slen && (s[sidx] == p[pidx] || p[pidx] == '.'))
            return tryMatch(s, sidx+1, p, pidx+1);
        else return false;
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
    if (p[plenm1] != '.' && p[plenm1] != '*' && p[plenm1] != s[slen-1]) return false;
    return tryMatch(s, 0, p, 0);
}
