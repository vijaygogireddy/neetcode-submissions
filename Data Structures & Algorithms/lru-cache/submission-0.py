class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0) #dummy
        # connect both
        self.left.next = self.right
        self.right.prev = self.left
        # left = LRU; right = MRU

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    def remove(self, node):
        # remove from doubly linked list
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def add(self, node):
        # add last
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
