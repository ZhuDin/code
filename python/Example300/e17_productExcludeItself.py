class Solution:
    def productExcludeItself(self, A):
        length, B = len(A), []
        f = [0 for i in range(length+1)]
        f[length] = 1
        for i in range(length-1, 0, -1):
            f[i] = f[i+1] * A[i]
        tmp = 1
        for i in range(length):
            B.append(tmp * f[i+1])
            tmp *= A[i]
        return B

if __name__ == "__main__":
    solution = Solution()
    A = [1, 2, 3, 4]
    B = solution.productExcludeItself(A)
    print("input:", A)
    print("output:", B)
    