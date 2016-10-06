#define isEndStr(c) ((c) == '\0')
#define aphaIdx(c) ((c) - 'a')
#define printf()

char* removeDuplicateLetters(char* s) {
    char *ret = malloc(27);
    char *na = calloc(26, 1);
    char *ea = calloc(26, 1);
    int i, j = 0;

    for (i=0; !isEndStr(s[i]); i++) na[aphaIdx(s[i])]++;
    for (i=0; !isEndStr(s[i]); i++) {
        printf("s[%d] %c\n", i, s[i]);
        if (j == 0) {
            ret[j++] = s[i];
            printf("push s[%d] %c on %d\n", i, s[i], j-1);
            ea[aphaIdx(s[i])] = 1;
        } else if (ea[aphaIdx(s[i])] == 0) {
            while(s[i] < ret[j-1] && na[aphaIdx(ret[j-1])] > 1) {
                printf("pop ret[%d] %c\n", j-1, ret[j-1]);
                na[aphaIdx(ret[j-1])]--;
                ea[aphaIdx(ret[j-1])] = 0;
                if (--j == 0) break;
            }
            ret[j++] = s[i];
            printf("push s[%d] %c on %d\n", i, s[i], j-1);
            ea[aphaIdx(s[i])] = 1;
        } else {
            na[aphaIdx(s[i])]--;
        }
    }
    ret[j] = '\0';
    return ret;
}
