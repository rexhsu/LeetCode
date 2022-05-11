class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
          a  e  i  o  u
    n=1   1  1  1  1  1  /a, e, i, o, u
    n=2   5  4  3  2  1  /a-> aa,ae,ai,ao,au | e-> ee,ei,eo,eu | i-> ii,io,iu | o-> oo,ou | u-> uu
    n=3   15 10 6  3  1
        """
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            o += u
            i += o
            e += i
            a += e
        return a+e+i+o+u