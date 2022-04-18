func findDuplicate(nums []int) int {
    var slow, fast int = nums[nums[0]], nums[nums[nums[0]]]
    for slow != fast {
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
