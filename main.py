import pygame, sys  # Pygame for game development, sys for system exit
import numpy as np  # Numpy for the game board matrix
import asyncio  # -- for web hosting purposes --

pygame.init()  # Initialize all pygame modules

# Constants for the game window and gameplay design
WIDTH = 800  # Window width (and height, since it's square)
HEIGHT = WIDTH  # Equal to width for a square window
LINE_WIDTH = 15  # Thickness of the grid lines
BOARD_ROWS = 3  # Number of rows in the Tic Tac Toe board
BOARD_COLS = 3  # Number of columns in the Tic Tac Toe board
SQUARE_SIZE = WIDTH // BOARD_COLS  # Size of each square in the grid
CIRCLE_RADIUS = SQUARE_SIZE // 3  # Radius of the circle for player 1
CIRCLE_WIDTH = 15  # Thickness of the circle
CROSS_WIDTH = 25  # Thickness of the cross for player 2
SPACE = SQUARE_SIZE // 4  # Space inside squares for cross drawing

# Colors (RGB tuples)
RED = (255, 0, 0)  # Example red color for debugging or future use
BG_COLOR = (28, 170, 156)  # Background color
LINE_COLOR = (23, 145, 135)  # Color of grid lines
CIRCLE_COLOR = (239, 231, 200)  # Color of the circle (player 1)
CROSS_COLOR = (66, 66, 66)  # Color of the cross (player 2)

# Create the game window and set its properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a display window
pygame.display.set_caption('TIC TAC TOE')  # Title of the window
screen.fill(BG_COLOR)  # Fill the background with the specified color

# Initialize the game board as a 3x3 matrix of zeros (empty squares)
board = np.zeros((BOARD_ROWS, BOARD_COLS)) 

# Function to draw the grid lines on the board
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw player figures (circle or cross) on the board
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # Player 1
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:  # Player 2
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 CROSS_WIDTH)

# Function to mark a square on the board for the current player
def mark_square(row, col, player):
    board[row][col] = player

# Check if a square is available
def available_square(row, col):
    return board[row][col] == 0

# Check if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:  # Empty square found
                return False
                
    return True

# Check if a player has won
def check_win(player):

    # Vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Ascending diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
        
    # Descending diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

# Functions to draw winning lines for different scenarios
def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal(player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

# Restart the game to its initial state
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    global player, game_over
    player = 1
    game_over = False
    board.fill(0)  # Reset the board to zeros

draw_lines()  # Draw the initial grid lines

player = 1  # Player 1 starts
game_over = False  # Track if the game is over

# Main game loop (asynchronous for web hosting purposes)
async def main():  # For asyncio compatibility
    global game_over, player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Exit the program
                
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                # Get click position
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                
                if available_square(clicked_row, clicked_col):  # Check if square is free
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):  # Check if the player wins
                        game_over = True
                        
                    player = player % 2 + 1  # Switch player
                    
                    draw_figures()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset game with 'R' key
                    restart()
                    game_over = False

                    print(board)

        pygame.display.update()  # Refresh the display

        # For asyncio compatibility
        await asyncio.sleep(0) # -- for web hosting purposes - Remove this to run regular python version

# Run the game loop asynchronously
asyncio.run(main()) # -- for web hosting purposes - Remove this to run regular python version

# uncomment this to run regular python version

# main()