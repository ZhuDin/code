class Solution:
    def findDiagonalOrder(self, matrix):
        import collections
        result = []
        dd = collections.defaultdict(list)
        if not matrix:
            return result
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j])
        for k, v in dd.items():
            if k % 2 == 1:dd[k].reverse()
            result += dd[k]
        return result

if __name__ == '__main__':
    m=[[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print('input:', m)
    print('output:', s.findDiagonalOrder(m))
    