class Solution:
    def movingStones(self, arr):
        arr = sorted(arr)
        even = 0
        odd = 0
        for i in range(0, len(arr)):
            odd += abs(arr[i]-(2*i+1))
            even += abs(arr[i]-(2*i+2))
        if odd < even:
            return odd
        return even

if __name__ == '__main__':
    arr = [1, 6, 7, 8, 9]
    solution = Solution()
    print("array:", arr)
    print("movingStone:", solution.movingStones(arr))
    