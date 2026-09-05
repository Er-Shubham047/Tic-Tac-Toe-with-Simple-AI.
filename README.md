# Tic-Tac-Toe with Minimax AI

A command-line Tic-Tac-Toe game written in Python where you play against an unbeatable computer opponent powered by the Minimax algorithm.

## Features

- Play as X against the computer (O)
- Computer uses the Minimax algorithm — it always plays optimally and never loses
- Board is displayed after every move
- Detects wins, losses, and draws correctly
- Option to play multiple rounds in a row

## How it works

The AI evaluates every possible future move using Minimax, a recursive algorithm that simulates all possible game outcomes to pick the move that maximizes its chances of winning (or forces a draw if a win isn't possible).

## Requirements

- Python 3.x

## How to run

```bash
python3 tic tac toe.py
```

## How to play

- You are `X`, the computer is `O`
- Enter a number from 1–9 to place your mark, corresponding to this layout:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

- The board updates after every move
- The game announces a win, loss, or draw at the end
- You'll be asked if you want to play again

## License

Free to use and modify.
