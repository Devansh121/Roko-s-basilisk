class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Create an 8x8 board with initial chess positions
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p"] * 8,
            ["."] * 8,
            ["."] * 8,
            ["."] * 8,
            ["."] * 8,
            ["P"] * 8,
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        return board

    def print_board(self):
        # Print the board to the console
        for row in self.board:
            print(" ".join(row))
        print()
    
    def get_pawn_moves(self, row, col):
        moves = []
        # Assuming white pawns (lowercase 'p' are black pawns)
        if self.board[row][col] == "P":
            if row > 0 and self.board[row-1][col] == ".":
                moves.append((row-1, col))  # Move forward
                if row == 6 and self.board[row-2][col] == ".":
                    moves.append((row-2, col))  # Initial two-square move
            # Capture diagonally
            if col > 0 and row > 0 and self.board[row-1][col-1].islower():
                moves.append((row-1, col-1))
            if col < 7 and row > 0 and self.board[row-1][col+1].islower():
                moves.append((row-1, col+1))
        return moves
    
    def get_knight_moves(self, row, col):
        moves = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for m in knight_moves:
            r, c = row + m[0], col + m[1]
            if 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == "." or self.board[r][c].islower():  # Empty or capture
                    moves.append((r, c))
        return moves
    
    def get_bishop_moves(self, row, col):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in directions:
            r, c = row, col
            while 0 <= r + d[0] < 8 and 0 <= c + d[1] < 8:
                r, c = r + d[0], c + d[1]
                if self.board[r][c] == ".":  # Empty square
                    moves.append((r, c))
                elif self.board[r][c].islower():  # Capture
                    moves.append((r, c))
                    break
                else:
                    break
        return moves

    def get_rook_moves(self, row, col):
        moves = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in directions:
            r, c = row, col
            while 0 <= r + d[0] < 8 and 0 <= c + d[1] < 8:
                r, c = r + d[0], c + d[1]
                if self.board[r][c] == ".":  # Empty square
                    moves.append((r, c))
                elif self.board[r][c].islower():  # Capture
                    moves.append((r, c))
                    break
                else:
                    break
        return moves
    
    def get_queen_moves(self, row, col):
        # Combine the moves of the rook and bishop
        return self.get_rook_moves(row, col) + self.get_bishop_moves(row, col)
    
    def get_king_moves(self, row, col):
        moves = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in directions:
            r, c = row + d[0], col + d[1]
            if 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == "." or self.board[r][c].islower():  # Empty or capture
                    moves.append((r, c))
        return moves
    

    
    def setup_test_position(self):
        # Clear the board
        self.board = [["."] * 8 for _ in range(8)]

        # Place white pawns and knights for testing
        self.board[6][4] = "P"  # White pawn
        self.board[7][1] = "N"  # White knight
        self.board[7][2] = "B"
        self.board[7][3] = "Q"
        self.board[7][4] = "K"
        self.board[7][0] = "R"

        # Place some black pieces to test captures
        self.board[5][5] = "p"  # Black pawn
        self.board[5][3] = "p"  # Another black pawn
        self.board[5][2] = "n"  # Black knight
        chess_board.print_board()

        # ... [within ChessBoard class] ...

    def mark_moves_on_board(self, moves):
        for move in moves:
            self.board[move[0]][move[1]] = '*'  # Mark the move
    
    def test_moves(self):
        # Setup a test position for each piece
        self.setup_test_position()

        # Test Pawn Moves
        print("Original Board:")
        self.print_board()
        print("Testing White Pawn Moves from E2:")
        pawn_moves = self.get_pawn_moves(6, 4)
        for move in pawn_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(pawn_moves)
        print("Board with Pawn Moves:")
        self.print_board()
        self.setup_test_position()  # Reset board

        # Test Knight Moves
        print("\nTesting White Knight Moves from B1:")
        knight_moves = self.get_knight_moves(7, 1)
        for move in knight_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(knight_moves)
        print("Board with Knight Moves:")
        self.print_board()
        self.setup_test_position()  # Reset board

        # Test Bishop Moves
        print("\nTesting White Bishop Moves from C1:")
        bishop_moves = self.get_bishop_moves(7, 2)
        for move in bishop_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(bishop_moves)
        print("Board with Bishop Moves:")
        self.print_board()
        self.setup_test_position()  # Reset board

        # Test Rook Moves
        print("\nTesting White Rook Moves from A1:")
        rook_moves = self.get_rook_moves(7, 0)
        for move in rook_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(rook_moves)
        print("Board with Rook Moves:")
        self.print_board()
        self.setup_test_position()  # Reset board

        # Test Queen Moves
        print("\nTesting White Queen Moves from D1:")
        queen_moves = self.get_queen_moves(7, 3)
        for move in queen_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(queen_moves)
        print("Board with Queen Moves:")
        self.print_board()
        self.setup_test_position()  # Reset board

        # Test King Moves
        print("\nTesting White King Moves from E1:")
        king_moves = self.get_king_moves(7, 4)
        for move in king_moves:
            print(f"Move to: {move}")
        self.mark_moves_on_board(king_moves)
        print("Board with King Moves:")
        self.print_board()




# Create an instance of the chess board and print it
chess_board = ChessBoard()
chess_board.print_board()

chess_board.test_moves()
chess_board.print_board()

