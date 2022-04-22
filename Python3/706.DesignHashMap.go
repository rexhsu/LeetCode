type MyHashMap struct {
    array [][2]int
}


func Constructor() MyHashMap {
    array := make([][2]int, 0, 10000)
    mhm := MyHashMap {
        array: array,
    }
    return mhm
}


func (this *MyHashMap) Put(key int, value int)  {
    for i,a := range(this.array) {
        if a[0] == key {
            this.array[i][1] = value
            return
        }
    }
    this.array = append(this.array, [2]int{key, value})
}


func (this *MyHashMap) Get(key int) int {
    for _,a := range(this.array) {
        if a[0] == key {
            return a[1]
        }
    }
    return -1
    
}

func (this *MyHashMap) Remove(key int)  {
    for i,a := range(this.array) {
        if a[0] == key {
            if i == len(this.array) - 1 { // tail of array
                this.array = this.array[:i]
            } else {
                this.array = append(this.array[:i], this.array[(i+1):]...)
            }
        }
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
