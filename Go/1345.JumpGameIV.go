func minJumps(arr []int) int {
    l := len(arr)
    if l==1 {
        return 0
    }
    m := make(map[int][]int)
    for idx,num := range(arr) {
        m[num] = append(m[num], idx)
    }
    
    v := make([]bool, 50000)
    queue := make([]int, 0, 50000)
    
    v[0] = true
    queue = append(queue, 0)
    
    level := 0
    
    for len(queue) > 0 {
        //fmt.Println("level queue", level, queue)
        ql := len(queue)
        for ql > 0 {
            idx := queue[0]
            //fmt.Println("now handle", e)
            queue = queue[1:] // pop an element
            if idx+1 < l && !v[idx+1] {
                v[idx+1] = true
                queue = append(queue, idx+1)
            }
            if idx > 0 && !v[idx-1] {
                v[idx-1] = true
                queue = append(queue, idx-1)
            }
            if idxs, found := m[arr[idx]]; found {
                for _,idx := range(idxs) {
                    if !v[idx] {
                        v[idx] = true
                        queue = append(queue, idx)
                    }
                }
                delete(m, arr[idx])
            }
            ql -= 1
        }
        level += 1
        if v[l-1] {
            return level
        }
    }
    
    return level
}
