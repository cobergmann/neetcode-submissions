class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                curr_value = board[r][c]
                if(
                    curr_value in rows[r] or
                    curr_value in cols[c] or
                    curr_value in boxes[(r//3, c//3)]
                ):
                    return False

                rows[r].add(curr_value)
                cols[c].add(curr_value)
                boxes[(r//3, c//3)].add(curr_value)
        return True