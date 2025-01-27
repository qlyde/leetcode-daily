class MyHashSet:
    # Time: O(1)
    # Space: O(1)

    def __init__(self):
        self.set = [0] * int(1e6 // 32 + 1)

    def add(self, key: int) -> None:
        self.set[key // 32] |= 1 << (key % 32)

    def remove(self, key: int) -> None:
        self.set[key // 32] &= ~(1 << (key % 32))

    def contains(self, key: int) -> bool:
        return self.set[key // 32] & (1 << (key % 32)) != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)