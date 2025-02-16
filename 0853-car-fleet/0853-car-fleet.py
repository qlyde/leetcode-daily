class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse=True)
        stack = []
        for p, s in ps:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
