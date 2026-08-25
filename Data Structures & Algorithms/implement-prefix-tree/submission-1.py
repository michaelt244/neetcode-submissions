class TrieNode:
    def __init__(self):
        self.childern = {}
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.childern:
                #if its not in the tree add it
                curr.childern[c] = TrieNode()
            curr = curr.childern[c]
        
        #marking it as a word once we add all the childern nodes
        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if c not in curr.childern:
                return False
            curr = curr.childern[c]
        #returning if the word is marked as finished
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.childern:
                return False
            curr = curr.childern[c]
        #we made it to the end so if there is still a childern it must start with that prefix
        return True
        
        