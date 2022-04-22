func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func canJump(nums []int) bool {
    goal  := len(nums) - 1
    farest := 0
    for i, n := range(nums) {
        if farest < i || farest >= goal {
            break
        }
        farest = max(i + n, farest)
    }
    return farest >= goal
}
