func canJump(nums []int) bool {
    i := 0
    l := len(nums)
    for i < (l - 1) { // stand before the last index
        jump := nums[i]
        if jump == 0 {
            return false
        }
        cur := i+jump
        farest := cur
        if farest >= (l - 1) { // beyond the last
            return true
        }
        //fmt.Println("for", i+1, i+jump)
        for j:=i+1; j < cur ; j++ {
            if j + nums[j] > farest {
                farest = j + nums[j]
            }
        }
        i = cur
        if i + nums[i] < farest {
            nums[i] = farest - i
        }
    }
    return true
}
