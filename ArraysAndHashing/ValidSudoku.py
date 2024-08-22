from typing import Counter, List


class Solution:

    def isValidList(self, unit):
        unit = [i for i in unit if i != "."]
        temp = set(unit)

        if len(temp) != len(unit):
            return False
        return True

    def checkBlock(self, board, startIndex):
        i, j = startIndex

        blockList = []
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                blockList.append(board[x][y])

        return self.isValidList(blockList)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidList(board[i][:]):
                return False
            if not self.isValidList([row[i] for row in board]):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkBlock(board, (i, j)):
                    return False
        return True


if __name__ == "__main__":
    temp = Solution().isValidSudoku(
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    print(temp)


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         seen = set()

#         for i in range(9):
#             for j in range(9):
#                 current_val = board[i][j]
#                 if current_val != '.':
#                     row_key = '{} in row {}'.format(current_val, i)
#                     col_key = '{} in col {}'.format(current_val, j)
#                     box_key = '{} in box {}-{}'.format(current_val, i // 3, j // 3)

#                     if (row_key in seen) or (col_key in seen) or (box_key in seen):
#                         return False

#                     seen.update([row_key, col_key, box_key])

#         return True
