from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack
