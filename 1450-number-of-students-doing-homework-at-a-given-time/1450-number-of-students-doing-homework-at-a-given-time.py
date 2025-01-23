class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # Time: O(n)
        # Space: O(1)
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res
