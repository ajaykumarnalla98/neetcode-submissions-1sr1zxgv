"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        def clone(node):
            if not node:
                return None
            if node in map:
                return map[node]
        
            copy = Node(node.val)
            map[node] = copy
            copy.next = clone(node.next)
            copy.random = clone(node.random)
            return copy
        
        return clone(head)