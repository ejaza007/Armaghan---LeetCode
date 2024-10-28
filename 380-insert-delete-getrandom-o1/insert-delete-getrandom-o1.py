import random

class RandomizedSet:

    def __init__(self):
        # Dictionary to store the index of each value for O(1) removal
        self.val_to_index = {}
        # List to store the values for O(1) random access
        self.data = []

    def insert(self, val: int) -> bool:
        # If the value already exists, return False
        if val in self.val_to_index:
            return False
        # Otherwise, add the value
        self.val_to_index[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If the value does not exist, return False
        if val not in self.val_to_index:
            return False
        # Swap the element to be removed with the last element
        last_element = self.data[-1]
        idx_to_remove = self.val_to_index[val]
        self.data[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove
        # Remove the last element from the list and dictionary
        self.data.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.data)
