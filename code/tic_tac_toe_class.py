# CS_372: Client-Server Chat/Game (Portfolio Assignment)
# tic_tac_toe_class.py
# Zachary Pilson
# pilsonz@oregonstate.edu

class tic_tac_toe:
    __board = [" "]*9
    __spaces = {"A1": 0, "A2": 1, "A3": 2,
                "B1": 3, "B2": 4, "B3": 5,
                "C1": 6, "C2": 7, "C3": 8,
                "a1": 0, "a2": 1, "a3": 2,
                "b1": 3, "b2": 4, "b3": 5,
                "c1": 6, "c2": 7, "c3": 8}
    __winningPossibilities = [[0,1,2],[3,4,5],[6,7,8],
                              [0,3,6],[1,4,7],[2,5,8],
                              [0,4,8],[2,4,6]]
    __player1 = 'X'
    __player2 = 'O'
    __player1_score = 0
    __player2_score = 0

    #########################################
    ##########- Private Functions -##########
    #########################################
    def __checkBoardStatus(self):
        """returns the status of the game: True if win or tie, or False if game is still going
        additionally resets the board if the game is over"""
        # Check for win
        for winPos in self.__winningPossibilities:
            if self.__board[winPos[0]] == self.__board[winPos[1]] == self.__board[winPos[2]] != " ":
                # returns winner: X or O
                winningPlayer = self.__board[winPos[0]]
                self.__adjustScore(winningPlayer)
                self.__resetBoard()
                return f"Player {winningPlayer} wins the game!"
        # Check if the game is still going
        for space in self.__board:
            if space == " ":
                return ""
        self.__resetBoard()
        return "Game was a tie"
    
    def __resetBoard(self):
        """removes all X's and O's from board"""
        for i in range(len(self.__board)):
            self.__board[i] = " "

    def __adjustScore(self, player):
        """Adds a point to winning players total score"""
        if player == self.__player1:
            self.__player1_score += 1
        else:
            self.__player2_score += 1

    def __insertCoord(self, player, coord):
        """inserts the given player coordinate into the position on the board.
        If successful, returns True, otherwise, returns False"""
        # Validate first
        if coord in self.__spaces:
            if self.__board[self.__spaces[coord]] == " ":
                self.__board[self.__spaces[coord]] = player
                return True
        return False

    #########################################
    ##############- Functions -##############
    #########################################  
    def startingMsg(self):
        # Prints a starting message
        print("-------Tic-Tac-Toe-------------------------------------------------------------")
        print("Get three in a row to win!")

    def printScore(self):
        # Prints the score of both player X and player O
        print(f"\nPlayer X score: {self.__player1_score}\nPlayer O score: {self.__player2_score}")

    def player1_move(self, coord):
        if self.__insertCoord(self.__player1, coord):
            self.printBoard()
            status_msg = self.__checkBoardStatus()
            return status_msg
        return "move was invalid"

    def player2_move(self, coord):
        if self.__insertCoord(self.__player2, coord):
            self.printBoard()
            status_msg = self.__checkBoardStatus()
            return status_msg
        return "move was invalid"

    def printBoard(self):
        # This will print out normally
        print(f"""
          1     2     3

             |     |
    A     {self.__board[0]}  |  {self.__board[1]}  |  {self.__board[2]}
        _____|_____|_____
             |     |
    B     {self.__board[3]}  |  {self.__board[4]}  |  {self.__board[5]}
        _____|_____|_____ 
             |     |
    C     {self.__board[6]}  |  {self.__board[7]}  |  {self.__board[8]}
             |     |
        """)
