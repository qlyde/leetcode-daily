class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        stack = []
        for asteroid in asteroids:
            if stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) < abs(asteroid):
                    while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                        stack.pop()
                    if stack and stack[-1] > 0 and abs(stack[-1]) == abs(asteroid):
                        stack.pop()
                    elif not stack or stack[-1] < 0:
                        stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack
