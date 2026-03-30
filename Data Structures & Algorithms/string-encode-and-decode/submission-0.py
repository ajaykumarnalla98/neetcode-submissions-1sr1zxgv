class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # find the separator '#'
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            # get the string of that length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length  # move to next encoded string
        return res