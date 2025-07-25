# Chess

A Python-based chess game aiming to replicate the experience of standard online platforms like [chess.com](https://chess.com). Currently under active development.

## Goal

This project is built to mimic a full-featured chess game, providing a playable board with legal move detection and a user-friendly interface using `pygame`.

---

## Current Features

- Detects legal moves for all standard chess pieces.
- Turn-based logic to ensure only the correct color can move.
- Interactive GUI using `pygame` and `pygame_widgets`.
- Visual indicators:
  - Dots: legal move tiles.
  - Circles: capture opportunities.
- Basic pawn promotion.

---

## Limitations (Work in Progress)

- No check/checkmate logic yet.
- No castling implemented.
- No en passant rule.
- No check detection or prevention.

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
   python display_board.py
   ```
