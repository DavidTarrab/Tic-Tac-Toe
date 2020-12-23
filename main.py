# Setup

# Board: 2D list
# empty_board, print_board, play_move

# Create empty board
dimX, dimY = 3, 3
def create_board(): 
  return [["-" for _ in range(dimX)] for _ in range(dimY)]

# Ask for player symbols
def get_symbols():
  error = True
  while error == True:
    p1s = input("Player 1's symbol: ")
    p2s = input("Player 2's symbol: ")
    print("\n")
    error = False
    if not p1s.isalpha() or not p2s.isalpha():
      error = True
      print("Use a letter")
    if p1s == p2s:
      error = True
      print("Choose different symbols")
    if error == True:
      print("\n")
  return p1s, p2s

# print board
def print_board(board):
  for row in board:
    for col in row:
      print(col, end=" ")
    print()

def play_move(board, player, row, col): 
  board [row] [col] = player

# get value of square
# output: X | O
def get_square(board, row, col):
  return board [row] [col]

# output X | O | None
def get_winner(board): 
  for player in [p1s, p2s]:
    # check each row
    for row in board: 
      if all(
        square == player  # condition
        for square in row  # for loop
      ): 
        return player

    for column in get_columns(board): 
      if all(
        square == player  # condition
        for square in column  # for loop
      ): 
        return player

    for diagonal in get_diagonals(board): 
      if all(
        square == player  # condition
        for square in diagonal  # for loop
      ): 
        return player
  else: return None
  
def get_columns(board): return [
  [  # element
    row [column_index]  # element
    for row in board  # for loop
  ]
  for column_index in range(3)  # for loop
]

# output: list of 2 lists
def get_diagonals(board): 
  # ( (0, 0), (1, 1), (2, 2) )
  diagonal1 = [board[index][index] for index in range(3)]
  # ( (0, 2), (1, 1), (2, 0) )
  diagonal2 = [board [row] [column] for row, column in enumerate(range(2, -1, -1))]
  return diagonal1, diagonal2

def check_tie(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "-":
        return None
  return "tie"


def check_game_state(board):
  if get_winner(board) != None:
    return "win"
  else: 
    if check_tie(board) == "tie":
      return "tie"
    else:
      return "midgame"

def get_move(board, player):
  validMove = False
  while validMove == False:

    error = True
    while error == True:
      moveRow = input("Row: ")
      moveCol = input("Col: ")
      error = False
      if not moveRow.isnumeric() or not moveCol.isnumeric():
        error = True
      else:
        moveRow = int(moveRow)
        moveCol = int(moveCol)
        if moveRow<1 or moveRow>3 or moveCol<1 or moveCol>3:
          error = True
      if error == True:
        print("\nUse either 1, 2, or 3\n")

    if board [moveRow-1] [moveCol-1] == "-":
      play_move(board, player, moveRow-1, moveCol-1)
      print("\n")
      validMove = True
    else:
      print("\nThat space is already taken\n")


p1s, p2s = get_symbols()

board = create_board()
print_board(board)
print("\n")
# Game

while check_game_state(board) == "midgame":
  turn = 1
  get_move(board, p1s)
  print_board(board)
  print("\n")
  if check_game_state(board) != "midgame":
    break
  turn = 2
  get_move(board, p2s)
  print_board(board)
  print("\n")
  check_game_state(board)

if check_game_state(board) == "tie":
  print("Tie!")
if check_game_state(board) == "win":
  print("Player", turn, "wins!")