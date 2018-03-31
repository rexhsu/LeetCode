class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.siz = len(board)
        self.solve()

    def findSlot(self):
        for i in range(self.siz):
            for j in range(self.siz):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1
        
    def solve(self):
        row, col = self.findSlot()
        if row == -1: return True
        nLst = range(1, 10)
        nLst = [str(c) for c in nLst]
        
        for n in nLst:
            #print row, col, n
            if self.solCheck(row, col, n):
                self.board[row][col] = n
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False           

    def solCheck(self, row, col, c):
        # row check
        if c in self.board[row]:
            #print c, " check false in", self.board[row]
            return False
        # col check
        for r in self.board:
            if r[col] == c:
                #print c, " check false in", r[col]
                return False
        # block check
        bs = int(self.siz ** 0.5)
        for i in range(row/bs*bs, row/bs*bs+bs):
            for j in range(col/bs*bs, col/bs*bs+bs):
                if self.board[i][j] == c:
                    #print c, " check false at ", i, ", ", j
                    return False
        return True
