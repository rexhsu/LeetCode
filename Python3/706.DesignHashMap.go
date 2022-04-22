type MyHashMap struct {
    array [][2]int
    siz int
}


func Constructor() MyHashMap {
    array := make([][2]int, 10000)
    mhm := MyHashMap {
        array: array,
        siz: 0,
    }
    return mhm
}


func (this *MyHashMap) Put(key int, value int)  {
    for i,a := range(this.array[0:this.siz]) {
        if a[0] == key {
            this.array[i][1] = value
            return
        }
    }
    this.array[this.siz] = [2]int{key, value}
    this.siz ++
}


func (this *MyHashMap) Get(key int) int {
    for _,a := range(this.array[0:this.siz]) {
        if a[0] == key {
            return a[1]
        }
    }
    return -1
    
}


func (this *MyHashMap) Remove(key int)  {
    for i,a := range(this.array[0:this.siz]) {
        if a[0] == key {
            if i != this.siz - 1 {
                this.array[i] = this.array[this.siz-1]
            }
            this.siz--
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
