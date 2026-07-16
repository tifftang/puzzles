class Node:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_word = ""
class Trie:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node(w)
            node = node.children[w]
        node.is_word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.insert(word)
        visited = set()
        result = set()
        def dfs(i, j, children):
            if board[i][j] not in children: return
            if children[board[i][j]].is_word:
                result.add(children[board[i][j]].is_word)
            visited.add((i, j))
            children = children[board[i][j]].children
            d = [(0, -1), (0, 1), (-1,0), (1, 0)]
            for x, y in d:
                new_i, new_j = i + x, j + y
                if new_i >= 0 and new_j >= 0 and new_i < len(board) and new_j < len(board[0]):
                    if board[new_i][new_j] in children and (new_i, new_j) not in visited:
                        dfs(new_i, new_j, children)
            visited.remove((i, j))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, t.root.children)
        return list(result)
