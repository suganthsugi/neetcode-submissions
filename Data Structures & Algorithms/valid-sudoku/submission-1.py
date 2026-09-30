class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tracker = {
            '0h': set([]),
            '1h': set([]),
            '2h': set([]),
            '3h': set([]),
            '4h': set([]),
            '5h': set([]),
            '6h': set([]),
            '7h': set([]),
            '8h': set([]),
            '0v': set([]),
            '1v': set([]),
            '2v': set([]),
            '3v': set([]),
            '4v': set([]),
            '5v': set([]),
            '6v': set([]),
            '7v': set([]),
            '8v': set([]),
            '0b': set([]),
            '1b': set([]),
            '2b': set([]),
            '3b': set([]),
            '4b': set([]),
            '5b': set([]),
            '6b': set([]),
            '7b': set([]),
            '8b': set([]),
        }
        def getBoxNumber(i, j):
            if (i>=0 and i<3) and (j>=0 and j<3):
                return '0b'
            if (i>=3 and i<6) and (j>=0 and j<3):
                return '1b'
            if (i>=6 and i<9) and (j>=0 and j<3):
                return '2b'
            if (i>=0 and i<3) and (j>=3 and j<6):
                return '3b'
            if (i>=3 and i<6) and (j>=3 and j<6):
                return '4b'
            if (i>=6 and i<9) and (j>=3 and j<6):
                return '5b'
            if (i>=0 and i<3) and (j>=6 and j<9):
                return '6b'
            if (i>=3 and i<6) and (j>=6 and j<9):
                return '7b'
            if (i>=6 and i<9) and (j>=6 and j<9):
                return '8b'
        
        for i in range(9):
            for j in range(9):
                h = f'{i}h'
                v = f'{j}v'
                val = board[i][j]
                box = getBoxNumber(i, j)
                if board[i][j] != '.' and (val in tracker[h] or val in tracker[v] or val in tracker[box]):
                    return False
                else:
                    tracker[h].add(val)
                    tracker[v].add(val)
                    tracker[box].add(val)
        return True