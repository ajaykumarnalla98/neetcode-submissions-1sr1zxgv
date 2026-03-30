class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.freq = 1
        self.prev = self.next = None   

class DLL:
    def __init__(self):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def add(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLRU(self):
        if self.size == 0: return None
        lru = self.tail.prev
        self.remove(lru)
        return lru

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minfreq = 0
        self.keymap = {} 
        self.freqmap = {}

    def update(self, node):
        freq = node.freq
        self.freqmap[freq].remove(node)

        if freq == self.minfreq and self.freqmap[freq].size == 0:
            self.minfreq += 1

        node.freq += 1
        if node.freq not in self.freqmap:
            self.freqmap[node.freq] = DLL()
        
        self.freqmap[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.keymap: return -1
        node = self.keymap[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        
        if key in self.keymap:
            node = self.keymap[key]
            node.val = value
            self.update(node)
            return
        
        if self.size == self.cap:
            lru = self.freqmap[self.minfreq].removeLRU()
            del self.keymap[lru.key]
            self.size -= 1
        
        node = Node(key, value)
        self.keymap[key] = node

        if 1 not in self.freqmap:
            self.freqmap[1] = DLL()
        
        self.freqmap[1].add(node)
        self.minfreq = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)