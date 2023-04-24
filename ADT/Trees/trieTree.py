class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value

    def lookup(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value

    def delete(self, key):
        def _delete(node, key, depth=0):
            if depth == len(key):
                node.value = None
                return len(node.children) == 0
            char = key[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], key, depth + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0
            return False
        _delete(self.root, key)

    def min(self):
        node = self.root
        while node.children:
            char = min(node.children.keys())
            node = node.children[char]
        return node.value

    def max(self):
        node = self.root
        while node.children:
            char = max(node.children.keys())
            node = node.children[char]
        return node.value
    
# trie = Trie()
# trie.insert("hello")
# trie.insert("")
# trie.insert("helloween")
# trie.insert("world")
# trie.insert("worlding")
# trie.insert("hi")

# print(trie.lookup("hello")) # True
# print(trie.lookup("hey")) # False

# trie.delete("hi")

# print(trie.lookup("hi")) # False

# print(trie.min()) # "hello"
# print(trie.max()) # "world"

trie = Trie()
trie.insert("apple", 1)
trie.insert("banana", 2)
trie.insert("orange", 3)

print(trie.lookup("apple"))  # 1
print(trie.lookup("banana"))  # 2
print(trie.lookup("orange"))  # 3
print(trie.lookup("grape"))  # None

trie.delete("banana")
print(trie.lookup("banana"))  # None

print(trie.min())  # 1
print(trie.max())  # 3
