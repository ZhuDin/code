class Solution:
    def findWords(self, words):
        res = []
        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for w in words:
            for j in range(3):
                flag = 1
                for i in w:
                    if i.lower() not in s[j]:
                        flag = 0
                        break
                if flag == 1:
                    res.append(w)
                    break
        return res

if __name__ == '__main__':
    word = ['Hello', "Alaska", 'Dad', "Peace"]
    s = Solution()
    print("input:", word)
    print("output:", s.findWords(word))
    