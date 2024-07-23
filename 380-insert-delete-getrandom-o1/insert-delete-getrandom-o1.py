import random

class RandomizedSet:

    def __init__(self):
        self.numSet = set()
        self.numArr = []

    def insert(self, val: int) -> bool:
        if val in self.numSet:
            return False
        else:
            self.numSet.add(val)
            self.numArr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.numSet:
            self.numSet.remove(val)
            self.numArr.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.numArr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()