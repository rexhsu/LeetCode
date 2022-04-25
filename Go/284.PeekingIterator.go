/*   Below is the interface for Iterator, which is already defined for you.
 *
 *   type Iterator struct {
 *       
 *   }
 *
 *   func (this *Iterator) hasNext() bool {
 *		// Returns true if the iteration has more elements.
 *   }
 *
 *   func (this *Iterator) next() int {
 *		// Returns the next element in the iteration.
 *   }
 */

type PeekingIterator struct {
    it *Iterator
    pn int
}

func Constructor(iter *Iterator) *PeekingIterator {
    pi := PeekingIterator{
        it: iter,
    }
    if pi.it.hasNext() {
        pi.pn = iter.next()
    } else {
        pi.pn = 0
    }
    
    return &pi
}

func (this *PeekingIterator) hasNext() bool {
    return this.pn != 0
}

func (this *PeekingIterator) next() int {
    ret := this.pn
    if this.it.hasNext() {
        this.pn = this.it.next()
    } else {
        this.pn = 0
    }
    return ret
}

func (this *PeekingIterator) peek() int {
    return this.pn
}
