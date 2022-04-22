func firstMissingPositive(nums []int) int {
    sort.Ints(nums)
    //fmt.Println(nums)
    mp := 1
    for _,n := range(nums) {
        if n > 0 {
            if n == mp {
                //fmt.Println("equal case", mp)
                mp++
            } else if n > mp {
                //fmt.Println("larger case", mp)
                break
            }
        }
    }
    
    return mp
}
