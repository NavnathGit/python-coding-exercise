
class Solution:
    def tictactoe(self, moves):
        n = 3
        board = [[0] * n for _ in range(n)]

        def checkRow(row, player_id):
            for col in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkDigonal(player_id):
            for row in range(n):
                if board[row][row] != player_id:
                    return False
            return True

        def checkAntiDigonal(player_id):
            for row in range(n):
                if board[row][n-1-row] != player_id:
                    return False
            return True

        player = 1
        for move in moves:
            row, col = move
            board[row][col] = player

            if checkRow(row, player) or checkCol(col, player) or (row == col and checkDigonal(player)) or (row + col == n-1 and checkAntiDigonal(player)):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == n*n else "Pending"


moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
obj = Solution()
print(obj.tictactoe(moves))

# Aproach 2


class Solution2:
    def tictactoe(self, moves):
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = antiDiag = 0

        player = 1
        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diag += player
            if row + col == n-1:
                antiDiag += player

            # abs gives absulote value of numbe i.e. distance from 0 abs(-5) = 5 also abs (5) = 5
            if any(abs(line) == n for line in (rows[row], cols[col], diag, antiDiag)):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == n*n else "Pending"
