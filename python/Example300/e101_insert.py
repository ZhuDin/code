class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def get(self):
        str1 = "(" + str(self.start) + "," + str(self.end) + ")"
        return str1
    def equals(self, Intervalx):
        if self.start == Intervalx.start and self.end == Intervalx.end:
            return 1
        else:
            return 0

class Solution:
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)
        return results
    
if __name__ == '__main__':
    solution = Solution()
    interval1 = Interval(1, 2)
    interval2 = Interval(5, 9)
    interval3 = Interval(2, 5)
    results = solution.insert([interval1, interval2], interval3)
    print("input:[", interval1.get(), ",", interval2.get(),"]", " ")
    print(interval3.get())
    print("output:[", results[0].get(), "]")
