**Tic Tac Toe – Python (4x4x4)**

This is a 3D Tic Tac Toe game implemented in Python using Tkinter for GUI. 
The player competes against an AI powered by the Minimax algorithm with alpha-beta pruning.
The game board consists of 4 layers, each with a 4x4 grid, represented seperately but interconnected.

**How to Play**
  The game starts with a prompt asking the player to choose a difficulty:

        easy → 2 levels of AI search
        difficult → 4 levels of AI search
        insane → 6 levels of AI search (more challenging and slower)

  The board is visually displayed as 4 side-by-side layers.
  Click on an empty cell to place your symbol (X).
  The AI (O) will respond immediately.
  The first to make 4 in a row (in any direction) wins.

**Winning Rules**
  You win by placing 4 of your symbols (X) in a line:
    Horizontally (within a layer)
    Vertically (within a layer)
    Pillars (same cell across layers)
    Diagonally (2D & 3D diagonals across the cube)

  The game will highlight the winning cells and show a popup if:
    You win
    AI wins
    It's a draw (board full, no winner)
   
