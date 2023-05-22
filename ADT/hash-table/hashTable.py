class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(self.size)]

    def hash_func(self, key):
        hashed = hash(key) % self.size
        return hashed

    def insert(self, key, value):
        hash_key = self.hash_func(key)
        for index, element in enumerate(self.hashmap[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.hashmap[hash_key][index] = (key, value)
                break
        else:
            self.hashmap[hash_key].append((key, value))

    def delete(self, key):
        hash_key = self.hash_func(key)
        for index, element in enumerate(self.hashmap[hash_key]):
            if element[0] == key:
                self.hashmap[hash_key].pop(index)
                break

    def get(self, key):
        hash_key = self.hash_func(key)
        for index, element in enumerate(self.hashmap[hash_key]):
            if element[0] == key:
                return element[1]

        raise KeyError(f"{key} does not exist")


h = HashTable()

h.insert(1, "one")
h.insert(2, "two")
h.insert("three", 3)

print(h.get(1))  # one
print(h.get(2))  # two
print(h.get("three"))  # 3

h.delete(2)

print(h.get(2))  # raises KeyError: 2 does not exist