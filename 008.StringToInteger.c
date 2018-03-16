int myAtoi(char* str) {
    int integerPart = 0;
    int oldIntPart = 0;
    int sign = 1;
    int numSign = 0;
    int intBegin = 0;
    int overflow = 0;

    if (!str || !*str) return 0; 

    for (; *str != '\0'; str++) {   
        if (*str == '-' || *str == '+') {
            numSign++;
            intBegin = 1;
            if (*str == '-')  sign = -1;
        } else if (*str >= '0' && *str <= '9') {
            oldIntPart = integerPart;
            integerPart = integerPart*10 + (*str - '0');
            if (integerPart / 10 != oldIntPart)
                overflow = 1;
            printf("%d overflow:%d\n", integerPart, overflow);
            intBegin = 1;
        } else if (*str == ' ' && intBegin == 0)
            continue;
        else
            break;
    }

    printf("%d %d", sign, integerPart);
    
    if (numSign > 1) return 0;
    if (overflow == 1) {
        if (sign == 1) return 2147483647;
        else return -2147483648;
    }
    return sign * (integerPart); 
}
