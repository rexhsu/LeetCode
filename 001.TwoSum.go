import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		j, ok := m[v]
		if ok {
            return []int{j, i}
        } else {
            m[target-v] = i
        }

	}
	return nil
}
