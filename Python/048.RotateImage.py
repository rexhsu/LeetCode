class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l/2):
            self.rotateOneLayer(matrix, i, l-i*2)
        
    def rotateOneLayer(self, matrix, off, siz):
        for pos in range(siz-1):
            tmp = matrix[off][off+pos]
            matrix[off][off+pos] = matrix[off+siz-1-pos][off]
            matrix[off+siz-1-pos][off] = matrix[off+siz-1][off+siz-1-pos]
            matrix[off+siz-1][off+siz-1-pos] = matrix[off+pos][off+siz-1]
            matrix[off+pos][off+siz-1] = tmp

