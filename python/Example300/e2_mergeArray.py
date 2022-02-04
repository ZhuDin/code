class Solution:
    # parm:
    # return:
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[i])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1  
        return C

if __name__ == '__main__':
    A = [1, 4]
    B = [1, 2, 3]
    D = [1, 2, 3, 4]
    E = [2, 4, 5, 6]
    solution = Solution()
    print("input:", A, " ", B)
    print("output:", solution.mergeSortedArray(A, B))
    print("input:", D, " ", E)
    print("output:", solution.mergeSortedArray(D, E))