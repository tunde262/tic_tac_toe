# Tic Tac Toe Game

A simple Tic Tac Toe game built with **Pygame** and **NumPy**. This project serves as a fun introduction to game development using Python and can optionally be hosted on the web using **asyncio** with the Pygbag library.

![thumbnail](https://github.com/tunde262/tic_tac_toe_game_python/blob/main/assets/thumbnail.png?raw=true)

## Features

- **Interactive Gameplay**: Play Tic Tac Toe with two players taking turns.
- **Win Detection**: Automatically detects wins (horizontal, vertical, or diagonal) and highlights the winning line.
- **Restart Functionality**: Reset the game at any time by pressing the `R` key.
- **Simple Design**: Clean interface with responsive grid and smooth drawing animations.
- **Optional Web Hosting**: The game can be hosted on the web using asyncio compatibility with the Pygbag library.

---

## Requirements
- Python 3.8+, recommended for the following reasons:
  1. **Enhanced `asyncio` Support**: The project uses `asyncio.run()` for the optional web-hosting feature, which simplifies asynchronous execution.
  2. **Compatibility with Pygbag**: Pygbag, used for web hosting, requires Python 3.8+.
- Pygame
- NumPy
- (Optional) Pygbag for web hosting

## Installation

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/tunde262/tic_tac_toe_game_python.git
   cd tic_tac_toe_game_python
   ```
   
3. **Install Dependencies**: Ensure you have Python 3.8+ installed. Then, install the required libraries:
   
   ```bash
   pip install pygame numpy
   ```

4. **Run the Game**:
   
   ```bash
   python main.py
   ```

---

## Web Hosting (Optional)

This project supports optional web hosting using `asyncio` and the **Pygbag** library.

1. **Install the Pygbag library**:
   ```bash
   pip install pygbag
   ```
   
2. **Compile and host the game**:
   ```bash
   pygbag main.py
   ```

3. Follow the output instructions to serve the game in a browser.

## How to Play

1. Start the Game: Run the script to open the game window.
2. Take Turns:
  - Player 1: Draws circles.
  - Player 2: Draws crosses.
3. Win the Game:
  - Get three symbols in a row, column, or diagonal to win.
4. Restart: Press the `R` key to reset the game board.

## Game Controls

- `Mouse`: Place a symbol
- `R`: 	Restart the game

---

## Future Enhancements
- Add an AI competitor.
- Mobile-friendly version with touch controls.
- Add on-screen instructions.

---

### Author
*Tunde Adepitan*  
GitHub: [tunde262](https://github.com/tunde262)  
Feel free to connect and give me feedback!
