class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f

        self.group[f].append(val)
        if f > self.maxFreq:
            self.maxFreq = f        

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()