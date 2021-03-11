class Board:
    x = 0
    y = 0
    two = 1
    three = 2
    four = 1
    five = 1
    board = []
    numout = {}
    def init(width, height):
    global board, x, y
    x = width
    y = height
    Columns = []
    for i in range(width):
        rows = []
        for i in range(height):
            numout[chr(97 + i)] = i
            slot = 0
            rows.append(slot)
        Columns.append(rows)
    board = Columns
def draw():
    start = 97
    for i in range(len(board)) :
      print( "    "+chr(start + i) ,end="")
    print("")
    for i in range(len(board)):
        for x in range(len(board)*5):
          print("-", end="")
        print("")
        print(str(i) + " |", end="")
        for j in range(len(board[i])):
            if board[i][j] == 0 or board[i][j] == 9:
                print(" O | " ,end="")
            if board[i][j] == 6:
                print(" m | " ,end="")
            if board[i][j] == 3:
                print(" h | " ,end="")

                
        print("")
        for x in range(len(board)*5):
          print("-", end="")
        print("")
                        
                #print("")

def boats():
    global two, three, four, five
    while True:
        if two == 0 and three == 0 and four == 0 and five == 0:
          break
        boat = input("Where do you want to place your boats?")
        letter = boat [0]
        number = int(boat [1])
        size = int(input("what size ship would you like?"))
        if size == 2 and two > 0:
            twoBoats(letter, number) 
        if size == 3 and three > 0:
            threeboats(letter, number)
        if size == 4 and four > 0:
            fourboats(letter, number)
        if size == 5 and five > 0:
            fiveboats(letter, number)
        draw() 

def fiveboats(letter, number):
  global five
  five -= 1
  direction = input("what direction do you want your boat in?")
  if direction == "down":
      if number + 4 < x:
          if board[number][numout[letter]] == 3 or board[number + 1][numout[letter]] == 3 or board[number + 2][numout[letter]] == 3 or board[number + 3][numout[letter]] or board[number + 4][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number + 1][numout[letter]] = 3
                board[number + 2][numout[letter]] = 3
                board[number + 3][numout[letter]] = 3
                board[number + 4][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")    
  if direction == "up":
      if number - 4 > -1:
          if board[number][numout[letter]] == 3 or board[number - 2][numout[letter]] == 3 or board[number - 1][numout[letter]] == 3 or board[number - 3][numout[letter]] == 3 or board[number - 4][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number - 1][numout[letter]] = 3
                board[number - 2][numout[letter]] = 3
                board[number - 3][numout[letter]] = 3
                board[number - 4][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "right":
      letter2 = chr(ord (letter) + 1)
      letter3 = chr(ord (letter) + 2)
      letter4 = chr(ord (letter) + 3)
      letter5 = chr(ord (letter) + 4)
      if ord(letter5) < 97 + y: 
          if board[number][numout[letter]] == 3 or board  [number][numout[letter2]] == 3 or board[number][numout[letter3]] or board[number][numout[letter4]] == 3 or board[number][numout[letter5]] == 3:

              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
                board[number][numout[letter4]] = 3
                board[number][numout[letter5]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "left":
      letter2 = chr(ord (letter) - 1)
      letter3 = chr(ord (letter) - 2)
      letter4 = chr(ord (letter) - 3)
      letter5 = chr(ord (letter) - 4)
      if ord(letter5) > 96:
          if board[number][numout[letter]] == 3 or board[number][numout[letter2]] == 3 or board[number][numout[letter3]] == 3 or board[number][numout[letter4]] == 3 or board[number][numout[letter5]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
                board[number][numout[letter4]] = 3
                board[number][numout[letter5]] = 3
      else:
          print("Error(Your ship is off the board)") 











def fourboats(letter, number):
  global four
  four -= 1
  direction = input("what direction do you want your boat in?")
  if direction == "down":
      if number + 3 < x:
          if board[number][numout[letter]] == 3 or board[number + 1][numout[letter]] == 3 or board[number + 2][numout[letter]] == 3 or board[number + 3][numout[letter]]:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number + 1][numout[letter]] = 3
                board[number + 2][numout[letter]] = 3
                board[number + 3][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")    
  if direction == "up":
      if number - 3 > -1:
          if board[number][numout[letter]] == 3 or board[number - 2][numout[letter]] == 3 or board[number - 1][numout[letter]] == 3 or board[number - 3][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number - 1][numout[letter]] = 3
                board[number - 2][numout[letter]] = 3
                board[number - 3][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "right":
      letter2 = chr(ord (letter) + 1)
      letter3 = chr(ord (letter) + 2)
      letter4 = chr(ord (letter) + 3)
      if ord(letter4) < 97 + y: 
          if board[number][numout[letter]] == 3 or board  [number][numout[letter2]] == 3 or board[number][numout[letter3]] or board[number][numout[letter4]] == 3:

              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
                board[number][numout[letter4]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "left":
      letter2 = chr(ord (letter) - 1)
      letter3 = chr(ord (letter) - 2)
      letter4 = chr(ord (letter) - 3)
      if ord(letter4) > 96:
          if board[number][numout[letter]] == 3 or board[number][numout[letter2]] == 3 or board[number][numout[letter3]] == 3 or board[number][numout[letter4]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
                board[number][numout[letter4]] = 3
      else:
          print("Error(Your ship is off the board)") 








def threeboats(letter, number):
  global three
  three -= 1
  direction = input("what direction do you want your boat in?")
  if direction == "down":
      if number + 2 < x:
          if board[number][numout[letter]] == 3 or board[number + 1][numout[letter]] == 3 or board[number +2][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number + 1][numout[letter]] = 3
                board[number + 2][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")    
  if direction == "up":
      if number - 2 > -1:
          if board[number][numout[letter]] == 3 or board[number - 2][numout[letter]] == 3 or board[number - 1][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number - 1][numout[letter]] = 3
                board[number - 2][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "right":
      letter2 = chr(ord (letter) + 1)
      letter3 = chr(ord (letter) + 2)
      if ord(letter3) < 97 + y: 
          if board[number][numout[letter]] == 3 or board  [number][numout[letter2]] == 3 or board[number][numout[letter3]]:

              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "left":
      letter2 = chr(ord (letter) - 1)
      letter3 = chr(ord (letter) - 2)
      if ord(letter3) > 96:
          if board[number][numout[letter]] == 3 or board[number][numout[letter2]] == 3 or board[number][numout[letter3]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
                board[number][numout[letter3]] = 3
      else:
          print("Error(Your ship is off the board)") 

def twoBoats(letter, number):
  global two
  two -= 1
  direction = input("what direction do you want your boat in?")
  if direction == "down":
      if number + 1 < x:
          if board[number][numout[letter]] == 3 or board[number + 1][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number + 1][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")    
  if direction == "up":
      if number - 1 > -1:
          if board[number][numout[letter]] == 3 or board[number - 1][numout[letter]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number - 1][numout[letter]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "right":
      letter2 = chr(ord (letter) + 1)
      if ord(letter2) < 97 + y: 
          if board[number][numout[letter]] == 3 or board[number][numout[letter2]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
      else:
          print("Error(Your ship is off the board)")

  if direction == "left":
      letter2 = chr(ord (letter) - 1)
      if ord(letter2) > 96:
          if board[number][numout[letter]] == 3 or board[number][numout[letter2]] == 3:
              print("Error(There is alredy a ship there)")
          else:
                board[number][numout[letter]] = 3
                board[number][numout[letter2]] = 3
      else:
          print("Error(Your ship is off the board)")  
  
            






    def guess(x,y):
        
        
                    

x = Board(5,5)
x.draw()
