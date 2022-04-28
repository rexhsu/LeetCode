func abs(x int) int{
    if x < 0 { return -x }
    return x
}

func reachGoal(heights [][]int, max int) bool {
    r, l := len(heights[0]), len(heights)
    queue := make([][2]int, 0, 100)
    var visited [100][100]int
    
    queue = append(queue, [2]int{0, 0})
    visited[0][0] = 1
    
    dir := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1},}
    
    for len(queue) > 0 {
        //fmt.Println(queue)
        x, y := queue[0][0], queue[0][1]
        if (x==l-1 && y==r-1) { return true }
        queue = queue[1:]
        for _, d := range(dir) {
            tx, ty := x+d[0], y+d[1]
            if (tx<0 || ty<0 || ty>r-1 || tx>l-1) { continue }
            if abs(heights[tx][ty] - heights[x][y]) > max { continue }
            if visited[tx][ty] == 1 { continue }
            queue = append(queue, [2]int{tx, ty})
            visited[tx][ty] = 1
        }
    }
    
    return false  
}

func minimumEffortPath(heights [][]int) int {
    left, right := 0, 1000000
    for left < right {
        var mid int = (left + right)/2
        if reachGoal(heights, mid) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}
