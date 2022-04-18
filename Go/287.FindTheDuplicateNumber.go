func findDuplicate(nums []int) int {
    slow, fast := nums[0], nums[0]
    for stop := true; stop ; stop = slow != fast {
        slow = nums[slow]
        fast = nums[nums[fast]]
    }
    fast = nums[0]
    for slow != fast {
        slow = nums[slow]
        fast = nums[fast]
    }
    return slow
}
