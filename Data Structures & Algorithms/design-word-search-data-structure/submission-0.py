class TreeNode:
    def __init__(self):
        self.child={}
        self.is_last=False

class WordDictionary:

    def __init__(self):
        self.root=TreeNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch]=TreeNode()
            curr=curr.child[ch]
        curr.is_last = True   # ✅ REQUIRED

        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]
                if c=='.':
                    for child in cur.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False

                    cur=cur.child[c]
            return cur.is_last
        return dfs(0,self.root)
            



                    

                    



            



        
