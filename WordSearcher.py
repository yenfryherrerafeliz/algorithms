"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
class WordSearcher(object):
    def __init__(self):
        self.map = {}

    def exist(self, board, word):
        self.buildMap(board)

        if len(word) == 1 and word in self.map:
            return True

        return self._exist(word, None, 0)
    
    def _exist(self, word, startPos, neighborIdx, visited={}):

        if neighborIdx == len(word):
            return True
        
        nPosLetter = word[neighborIdx]
        nPositions = []
        
        if nPosLetter in self.map:
            nPositions = self.map[nPosLetter]
            
        for nPos in nPositions:

            vKey = nPosLetter + '-' + str(nPos)

            if vKey in visited and visited[vKey] == True:
                continue
            
            if startPos is None or self.areNeighbors(startPos, nPos):

                if vKey not in visited or visited[vKey] == False:
                    visited[vKey] = True
                    
                exist = self._exist(word, nPos, neighborIdx + 1, visited)

                if exist:
                    return True
            

        for key in visited:
            visited[key] = False
            
        return False
    
    def areNeighbors(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])== 1
    
    def buildMap(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                elm = board[row][col]

                if elm not in self.map:
                    self.map[elm] = []
    
                self.map[elm].append((row, col))

if __name__ == '__main__':

    tests = [
        {'input': {'board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'word': 'ABCCED'}, 'expect': True},
        {'input': {'board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'word': 'SEE'}, 'expect': True},
        {'input': {'board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'word': 'ABCB'}, 'expect': False},
        {'input': {'board': [["a", "a"]], 'word': 'aaa'}, 'expect': False},
        {'input': {'board': [["a","b"],["c","d"]], 'word': "cdba"}, 'expect': True},
    ]

    for test in tests:
        wSearcher = WordSearcher()
        result = wSearcher.exist(test['input']['board'], test['input']['word'])

        print('Input: ', '', ', Result: ', result, ', Expected: ', test['expect'], ', Test Passed: ', result == test['expect'])
        
