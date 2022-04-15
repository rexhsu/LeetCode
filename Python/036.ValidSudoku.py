class Solution(object):  
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        siz = len(board)
        numLst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # row validation
        for r in board:
            t = list(numLst)
            for b in r:
                if b != '.':
                    if b in t:
                        t.remove(b)
                    else:
                        #print "row validate false: ", r, " at ", b
                        return False
        # column validation
        for c in range(siz):
            t = list(numLst)
            for r in board:
                b = r[c]
                if b != '.':
                    if b in t:
                        t.remove(b)
                    else:
                        #print "column validate false: ", r, " at ", b
                        return False
        # 3x3 validattion
        for i in range(0, siz, 3):
            for j in range(0, siz, 3):
                t = list(numLst)
                bLst = [board[i][j], board[i+1][j], board[i+2][j], 
                        board[i][j+1], board[i+1][j+1], board[i+2][j+1],
                        board[i][j+2], board[i+1][j+2], board[i+2][j+2]]
                for b in bLst:
                    if b != '.':
                        if b in t:
                            t.remove(b)
                        else:
                            #print "3x3 validate false: ", bLst, " at ", b
                            return False
        return True
