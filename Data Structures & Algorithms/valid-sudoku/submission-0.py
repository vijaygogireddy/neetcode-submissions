class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                curr_key = board[r][c]

                if curr_key == '.':
                    continue

                if (curr_key in rows[r] or curr_key in cols[c] or 
                    curr_key in squares[(r//3, c//3)]):
                    return False

                rows[r].add(curr_key)
                cols[c].add(curr_key)
                squares[(r//3, c//3)].add(curr_key)

        return True

                