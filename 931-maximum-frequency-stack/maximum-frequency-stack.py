class FreqStack:
    def __init__(self):
        self.freq = {}  # Dictionary to store the frequency of each element
        self.group = {}  # Dictionary to store stacks of elements by their frequency
        self.maxfreq = 0  # Variable to keep track of the current maximum frequency

    def push(self, val: int) -> None:
        # Increment the frequency of the element
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        # Update the maximum frequency
        if f > self.maxfreq:
            self.maxfreq = f
        # Push the element onto the stack corresponding to its frequency
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self) -> int:
        # Pop the element from the stack corresponding to the current maximum frequency
        val = self.group[self.maxfreq].pop()
        # Decrement the frequency of the element
        self.freq[val] -= 1
        # If the stack for the maximum frequency is empty, decrement the maximum frequency
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val

# Example usage:
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())  # Output: 5 (5 is the most frequent)
print(freqStack.pop())  # Output: 7 (5 and 7 are tied, 7 is closest to top)
print(freqStack.pop())  # Output: 5 (5 is now the most frequent again)
print(freqStack.pop())  # Output: 4 (remaining elements are 4 and 7, 4 is closest to top)
