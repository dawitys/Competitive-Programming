class Node:
    childNodes = None
    isFilled = False
    isWord = False
    val = None
    def __init__(self, x):
        self.isFilled = False
        self.isWord = False
        self.val = chr(ord('a')+x)
        
    def addChildren(self) -> None:
        if not self.childNodes:
            self.childNodes = [Node(x) for x in range(26)]

    def getChild(self, word, idx):
        return self.childNodes[ord(word[idx])-ord('a')] if self.childNodes else None

    def insert(self, word: str, idx: int) -> None:
        if len(word) == idx:
            self.isWord = True
            return
        self.addChildren()
        node = self.getChild(word, idx)
        node.isFilled = True
        return node.insert(word, idx+1)
    
    def search(self, word: str, idx:int) -> bool:
        if not self.isFilled: return False
        if len(word) == idx:
            return self.isWord
        node = self.getChild(word, idx)
        return node.search(word, idx+1) if node else False

    def startsWith(self, prefix: str, idx:int) -> bool:
        if not self.isFilled: return False
        if len(prefix) == idx:
            return True
        node = self.getChild(prefix, idx)
        return node.startsWith(prefix, idx+1) if node else False
        
    def __str__(self):
        return "{} Filled: {} Word: {}".format(self.val, self.isFilled, self.isWord)
    
class Trie:
    root = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        self.root.isFilled = True
        self.root.addChildren()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root.insert(word, 0)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.root.search(word, 0)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.startsWith(prefix, 0)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
