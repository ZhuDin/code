class Solution:
    # param:
    # return:
    def countSegments(self, s):
        res = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1]==' '):
                res += 1
        return res
    
if __name__ == '__main__':
    s = Solution()
    n = "Hello, my name is John"
    print("input:", n)
    print("output:", s.countSegments(n))
    