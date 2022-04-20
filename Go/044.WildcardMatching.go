func isMatch(s string, p string) bool {
    // dp[i][j]: p[0:j] can be matched by s[0:i]
    var dp[2000][2000]bool
    
    s = "#" + s
    p = "#" + p
    
    dp[0][0] = true // empty string match empty string
    
    // handle dp[0][1..n]
    for x:=1; x<len(p); x++ {
        //fmt.Printf("p[%d] is %c", x, p[x])
        if p[x] != '*' {
            break;
        }
        dp[0][x] = true
    }
    
    for i:=1; i<len(s); i++ {
        for j:=1; j<len(p); j++{
            if p[j] == '?' { // ? means one word ahead matching
                dp[i][j] = dp[i-1][j-1]
            } else if p[j] == '*' {
                /*
                for k:=0; k<=i; k++ {
                    if dp[k][j-1] == 1 {
                        dp[i][j] = 1
                    }
                }
                */
                dp[i][j] = dp[i][j-1] || dp[i-1][j]
            } else if s[i] == p[j] {
                dp[i][j] = dp[i-1][j-1]
            }
        }
    }
    /*
    for i:=0; i<len(s); i++ {
        for j:=0; j<len(p); j++{
            fmt.Print(dp[i][j], " ")
        }
        fmt.Println()
    }
    */
    
    return dp[len(s)-1][len(p)-1]
}
