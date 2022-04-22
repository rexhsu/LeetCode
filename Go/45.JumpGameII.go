func jump(nums []int) int {
    min := make([]int, 10000)
    goal := len(nums)-1 
    if goal == 0 {
        return 0
    }
    for i, n := range(nums) {
        if i+n >= goal {
            return min[i]+1
        }
        for j:=i+1; j<=i+n; j++ {
            if min[j] == 0 || min[j] > min[i] + 1 {
                min[j] = min[i] + 1
            }
        }
    }
    return min[goal]
}
