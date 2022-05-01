class TicTacToe():
    
    def __init__(self):
        self.grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.turn = 1
    
    def whosMove(self):
        if self.turn == 1:
            self.turn =2 
        elif self.turn == 2:
            self.turn = 1

    def move(self, place):
        if self.turn == 1:
            if place == 1:
                self.grid[0][0] = "X"
            elif place == 2:
                self.grid[0][1] = "X"
            elif place == 3:
                self.grid[0][2] = "X"
            elif place == 4:
                self.grid[1][0] = "X"
            elif place == 5:
                self.grid[1][1] = "X"
            elif place == 6:
                self.grid[1][2] = "X"
            elif place == 7:
                self.grid[2][0] = "X"
            elif place == 8:
                self.grid[2][1] = "X"
            elif place == 9:
                self.grid[2][2] = "X"
        elif self.turn == 2:
            if place == 1:
                self.grid[0][0] = "O"
            elif place == 2:
                self.grid[0][1] = "O"
            elif place == 3:
                self.grid[0][2] = "O"
            elif place == 4:
                self.grid[1][0] = "O"
            elif place == 5:
                self.grid[1][1] = "O"
            elif place == 6:
                self.grid[1][2] = "O"
            elif place == 7:
                self.grid[2][0] = "O"
            elif place == 8:
                self.grid[2][1] = "O"
            elif place == 9:
                self.grid[2][2] = "O"
    
    def checkWinner(self):

        for row in range(3):
            if self.grid[row] == ["X", "X", "X"]:
                print("Player 1 has won!")
                return True
            elif self.grid[row] == ["O", "O", "O"]:
                print("Player 2 has won!")
                return True

        for i in range(3):
            counter = 0
            for j in range(3):
                if self.grid[j][i] == "X":
                    counter += 1
            if counter == 3:
                print("Player 1 has won!")
                return True
        for i in range(3):
            counter = 0
            for j in range(3):
                if self.grid[j][i] == "O":
                    counter += 1
            if counter == 3:
                print("Player 2 has won!")
                return True

        diagonal_counter = 0
        diagonal_counter2 = 0
        for i in range(3):
            if self.grid[i][2-i] == "X":
                 diagonal_counter += 1
            if self.grid[i][i] == "X":
                 diagonal_counter2 += 1
            if  diagonal_counter == 3 or  diagonal_counter2 == 3:
                print("Player 1 has won!")
                return True
        diagonal_counter = 0
        diagonal_counter2 = 0
        for i in range(3):
            if self.grid[i][2-i] == "O":
                diagonal_counter += 1
            if self.grid[i][i] == "O":
                diagonal_counter2 += 1
            if diagonal_counter == 3 or diagonal_counter2 == 3:
                print("Player 2 has won!")
                return True
        return False

    def __str__ (self):
            board = ""
            for row in self.grid:
                for place in row:
                    board += str(place) + "|"
                board += "\n"
                board += "------"
                board += "\n"
            return board
            
    def checktie(self):
        tie_found = True
        for row in range(3):
            for column in range(3):
                if self.grid[row][column] != "X" and self.grid[row][column] != "O":
                    tie_found = False
        if tie_found:
            print("\n")
            print("The game is a tie!")
            return True
        return False

print("Welcome to TicTacToe!" + "\n" +"This is a two player game and the rules are:" + "\n" + "-Each player must take a turn to select a box on the grid"+ "\n" + 
 "-The first player will be X and the second one will be O"+ "\n" +"-To select where place your turn you will have to enter a number corresponding to the place on the grid"+ "\n" +
 "-The grid below shows what box corresponds to which number" + "\n" + "GOOD LUCK!")

print("|1|2|3|"+ "\n" +"--------"+ "\n" + "|4|5|6|"+ "\n" +"--------"+ "\n" + "|7|8|9|")
start = TicTacToe()
moves = []
while ((start.checkWinner() == False ) and (start.checktie() == False)):
    while True:
        try:
            place = int(input("Where do you want to place? "))
        except Exception:
            print("Invalid input try again!")
        else:
            if place < 1 or place > 9:
                print("Invalid input try again!")
            elif place in moves:
                print("Invalid input already placed there, try again!")
            else:
                break
    moves.append(place)
    start.move(place)
    start.whosMove()
    print(start)
