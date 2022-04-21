type MyHashSet struct {
    array []int
    siz int 
}


func Constructor() MyHashSet {
    array := make([]int, 10000)
    mhs := MyHashSet {
        array: array,
        siz: 0,
    }
    return mhs
}


func (this *MyHashSet) Add(key int)  {
    //fmt.Print(this.array)
    this.array[this.siz] = key
    this.siz++
}


func (this *MyHashSet) Remove(key int)  {
    if this.siz == 0 {
        return
    }
    for i,num := range(this.array[:this.siz]) {
        if key == num {
            if /*this.siz != 1 &&*/ i != this.siz - 1{
                this.array[i] = this.array[this.siz-1]
            }
            this.siz--
        }
    }
}


func (this *MyHashSet) Contains(key int) bool {
    for _,num := range(this.array[:this.siz]) {
        if key == num {
            return true
        }
    }
    return false
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
