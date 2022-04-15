bool isMatch(char* s, char* p) {
    int i = 0, j = 0, star = -1, mark = -1, slen = strlen(s), plen = strlen(p);
    while (i < slen) {
        if (j < plen && (p[j] == '?' || p[j] == s[i])) {
            ++i;
            ++j;
        } else if (j < plen && p[j] == '*') {
            star = j;
            j++;
            mark = i;
        } else if (star != -1) {
            j = star + 1;
            i = ++mark;
        } else return false;
    }
    while (j < plen && p[j] == '*') ++j;
    return j == plen;
}
