class Solution:
    def modernLudo(self, length, connections):
        ans = [i for i in range(length+1)]
        for i in range(length+1):
            for j in range(1,7):
                if(i-j >= 0):
                    ans[i] = min(ans[i], ans[i-j]+1)
            for j in connections:
                if(i==j[1]):
                    ans[i] = min(ans[i], ans[j[0]])
        return ans[length]

if __name__ == '__main__':
    length = 15
    connections = [[2,8], [6,9]]
    solution = Solution()
    print("Ludo length:", length)
    print("connection:", connections)
    print("result:", solution.modernLudo(length, connections))
    