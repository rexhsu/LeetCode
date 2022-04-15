#define ANSCII_0 47
#define ANSCII_9 57
#define ANSCII_A 43
#define ANSCII_M 45
#define ANSCII_Dot 46
#define ANSCII_e 101
#define ANSCII_Space 32

#define IsNum(c) ((c) >= ANSCII_0 && (c) <= ANSCII_9)

bool isNumber(char* s) {
    int slen = strlen(s), i=0;
    for (; i<slen; i++) {
        if (s[i] == ANSCII_Space) continue;
        if (IsNum(s[i])) goto NUM0;
        if (s[i] == ANSCII_Dot) goto DOT0;
        if (s[i] == ANSCII_M || s[i] == ANSCII_A) goto SIG0;
        return false;
    }
    return false;
SIG0:
    i++;
    for (; i<slen; i++) {
        if (IsNum(s[i])) goto NUM0;
        if (s[i] == ANSCII_Dot) goto DOT0;
        return false;
    }
    return false;
NUM0:
    for (; i<slen; i++) {
        if (IsNum(s[i])) continue;
        if (s[i] == ANSCII_Dot) goto DOT1;
        if (s[i] == ANSCII_e) goto EXP0;
        if (s[i] == ANSCII_Space) goto TAIL;
        return false;
    }
    goto RET;
DOT0:
    i++;
    for (; i<slen; i++) {
        if (IsNum(s[i])) goto NUM1;
        return false;
    }
    return false;
DOT1:
    i++;
    for (; i<slen; i++) {
        if (IsNum(s[i])) goto NUM1;
        if (s[i] == ANSCII_e) goto EXP0;
        if (s[i] == ANSCII_Space) goto TAIL;
        return false;
    }
    goto RET;
EXP0:
    i++;
    for (; i<slen; i++) {
        if (IsNum(s[i])) goto NUM2;
        if (s[i] == ANSCII_M || s[i] == ANSCII_A) goto SIG1;
        return false;
    }
    return false;
SIG1:
    i++;
    for (; i<slen; i++) {
        if (IsNum(s[i])) goto NUM2;
        return false;
    }
    return false;
NUM1:
    for (; i<slen; i++) {
        if (IsNum(s[i])) continue;
        if (s[i] == ANSCII_e) goto EXP0;
        if (s[i] == ANSCII_Space) goto TAIL;
        return false;
    }
    goto RET;
NUM2:
    for (; i<slen; i++) {
        if (IsNum(s[i])) continue;
        if (s[i] == ANSCII_Space) goto TAIL;
        return false;
    }
    goto RET;
TAIL:
    for (; i<slen; i++) {
        if (s[i] == ANSCII_Space) continue;
        return false;
    }
RET:
    if (i == slen) return true;
    else return false;
}
