func jump(nums []int) int {   
    goal := len(nums)-1
    if goal == 0 {
        return 0
    }
    res, cur, max := 0, 0, 0
    for i, n := range(nums[:goal]) {
        if i+n > max {
            max = i+n
        }
        if i == cur {
            res ++
            cur = max
        }
    }
    return res
}
