class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 1
        direction = 1

         
        while time > 0:
            index+=direction
            if index == n or index == 1:
                direction = -direction
            time-=1
        return index


        

        