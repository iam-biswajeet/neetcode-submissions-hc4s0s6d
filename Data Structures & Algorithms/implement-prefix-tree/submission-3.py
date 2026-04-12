class TreeNode:
    def __init__(self):
        self.child={}
        self.is_last=False




class PrefixTree:


    def __init__(self):
        self.root=TreeNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for ch in word:
            if ch not in cur.child :
                cur.child[ch]=TreeNode()
            cur=cur.child[ch]
        cur.is_last=True
            


    def search(self, word: str) -> bool:
        cur=self.root
        for ch in word:
            if ch not in cur.child :
                return False
            cur=cur.child[ch]
        if cur.is_last:
            return True
        else:
            return False
        
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for ch in prefix:
            if ch not in cur.child :
                return False
            cur=cur.child[ch]
        return True
        