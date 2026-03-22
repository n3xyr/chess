# Chess

A Python-based chess game aiming to replicate the experience of standard online platforms like [chess.com](https://chess.com). Currently, this project is kind of abandoned and it may stay that way forever.

WARNING: this is a While In Progress project, so you will find bugs. It's also our first project so the code is terrible. >e never intended to do a full release, but more of a fun project to learn python and things around project creation.

## Goal

This project is built to mimic a full-featured chess game, providing a playable board with legal move detection and a user-friendly interface using `pygame`.

---

## Current Features

- A fully functionning chess game.
- Game menu with clock settings.
- Detects legal moves for all standard chess pieces.
- Interactive GUI using `pygame` and `pygame_widgets`.
- Visual indicators:
  - Dots: legal move tiles.
  - Circles: capture opportunities.
- Game historic with notations.

---

## Limitations (Work in Progress)

- No premoves available.
- Unable to drag pieces to move them.
- Checkmate isn't detected sometimes

---

## Tech Stack

- Python (3.x)
- [`pygame`](https://www.pygame.org/)
- `pygame_widgets`
- `screeninfo`
- `time`, `datetime`, `sys`

---

## Installation & Running

1. Clone the repo

   ```bash
   cd chess
   git clone https://github.com/n3xyr/chess.git
   ```

2. Install Python 3.x
3. Run `setup.bat` to install dependencies.
4. Start the game:

   ```bash
   python menu.py
   ```