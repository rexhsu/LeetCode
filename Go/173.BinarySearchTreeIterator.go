/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type BSTIterator struct {
    stack []*TreeNode
}


func Constructor(root *TreeNode) BSTIterator {
    stack := make([]*TreeNode, 0, 128)
    res := BSTIterator {
        stack: stack,
    }
    res.push(root)
    return res
}


func (this *BSTIterator) Next() int {
    size := len(this.stack)
    var top *TreeNode
    this.stack, top = this.stack[:size-1], this.stack[size-1]
    this.push(top.Right)
    return top.Val
}


func (this *BSTIterator) HasNext() bool {
    return len(this.stack) > 0
}

func (this *BSTIterator) push(root *TreeNode) {
    for root != nil {
        this.stack = append(this.stack, root)
        root = root.Left
    }
}


/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
