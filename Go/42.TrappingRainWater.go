func Max(x, y int) int {
    if x < y {
        return y
    }
    return x
}

func trap(height []int) int {
    l, r := 0, len(height)-1 
    //fmt.Print(l, r)
    max_l := height[l]
    max_r := height[r]
    ans := 0
    
    for l < r {
        //fmt.Println(max_l, max_r, height[l], height[r])
        if max_l < max_r {
            ans += max_l - height[l]
            max_l = Max(max_l, height[l+1])
            l++
        } else {
            ans += max_r - height[r]
            max_r = Max(max_r, height[r-1])
            r--
        }
        //fmt.Println("ans", ans)
    }
    return ans
}
