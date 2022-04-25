type Item struct {
    score int
    index int
}

type Heap []Item
func (h Heap) Len() int             { return len(h) }
func (h Heap)   Less(i, j int) bool { return h[i].score > h[j].score }
func (h Heap) Swap(i, j int)        { h[i], h[j] = h[j], h[i] }

func (h *Heap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
    *h = append(*h, x.(Item))
}

func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxResult(nums []int, k int) int {
    N := len(nums)
    if N == 1 {
        return nums[0]
    }
    h := &Heap{Item{
        score: nums[0],
        index: 0,
    }}
    for i := 1; i < N; i++ {
        //fmt.Println(h)
        item := heap.Pop(h)
        //fmt.Println("index", item.(Item).index)
        for item.(Item).index < i-k {
            item=heap.Pop(h)
        }
        heap.Push(h, item)
        //fmt.Println("item num", item, nums[i])
        if i == N-1 {
            return item.(Item).score + nums[i]
        }
        heap.Push(h, Item{
            score: item.(Item).score + nums[i],
            index: i,
        })
    }

    return 0
}
