class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = {}
        for i in range(len(order)):
            ordermap[order[i]] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]

                if ordermap[char1] < ordermap[char2]:
                    break
                elif ordermap[char1] > ordermap[char2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True