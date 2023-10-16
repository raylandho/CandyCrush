import pygame
import random
from constants import ROWS, COLS, CELL_SIZE, window_size

class Board:
    def __init__(self):
        self.board = [[random.randint(1, 5) for _ in range(COLS)] for _ in range(ROWS)]
        self.calculate_board_position()

    def calculate_board_position(self):
        # Calculate the position to center the board horizontally and vertically
        board_width = COLS * CELL_SIZE[0]
        board_height = ROWS * CELL_SIZE[1]
        self.x = (window_size[0] - board_width) // 2
        self.y = (window_size[1] - board_height) // 2

    def swap_candies(self, row1, col1, row2, col2):
        # Swap tiles at (row1, col1) and (row2, col2) on the board
        #print(self.board[row1][col1])
        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]
        #print(self.board[row1][col1])

    def check_matches(self):
        # Check for horizontal matches
        for row in range(ROWS):
            for col in range(COLS - 2):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2]:
                    # Cascade tiles above
                    curr_row = row
                    while curr_row > 0:
                        self.board[curr_row][col] = self.board[curr_row - 1][col]
                        self.board[curr_row][col + 1] = self.board[curr_row - 1][col + 1]
                        self.board[curr_row][col + 2] = self.board[curr_row - 1][col + 2]
                        curr_row -= 1
                    # Refill the top row with random values
                    self.board[0][col] = random.randint(1, 5)
                    self.board[0][col + 1] = random.randint(1, 5)
                    self.board[0][col + 2] = random.randint(1, 5)

    def initialize_board(self):
        # Initialize the game board logic here
        pass

    def draw_board(self, screen, selected_tile=None, mouse_pos=None):
        for row in range(ROWS):
            for col in range(COLS):
                # 1: red 2: green 3: blue 4: yellow 5: purple
                if self.board[row][col] == 1:
                    color = (255, 0, 0)
                elif self.board[row][col] == 2:
                    color = (0, 255, 0)
                elif self.board[row][col] == 3:
                    color = (0, 0, 255)
                elif self.board[row][col] == 4:
                    color = (255, 255, 0)
                elif self.board[row][col] == 5:
                    color = (255, 0, 255)

                tile_size = min(CELL_SIZE)  # Ensure the tile size is the smaller of the two dimensions (width and height)
                x = self.x + col * tile_size  # Calculate the x-coordinate of the current tile
                y = self.y + row * tile_size  # Calculate the y-coordinate of the current tile

                # Draw the tile
                pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

                # Add black borders around the tiles
                border_color = (0, 0, 0)  # Border color: black
                border_width = 2  # Border width: 2px
                pygame.draw.rect(screen, border_color, (x, y, tile_size, tile_size), border_width)

                # Check if mouse is hovering the tile and draw a border around it
                if mouse_pos and x <= mouse_pos[0] <= x + tile_size and y <= mouse_pos[1] <= y + tile_size:
                    temp_border_color = (255, 255, 255)
                    temp_border_width = 4
                    pygame.draw.rect(screen, temp_border_color, (x, y, tile_size, tile_size), temp_border_width)

                # Check if the current tile is the selected tile, and if so, draw a border around it
                if (row, col) == selected_tile:
                    selected_border_color = (255, 255, 255)  # Border color for selected tile: white
                    selected_border_width = 4  # Border width for selected tile: 4px
                    pygame.draw.rect(screen, selected_border_color, (x, y, tile_size, tile_size), selected_border_width)

    def update_board(self):
        # Update the game board logic here
        pass

    def is_game_over(self):
        # Check for game over conditions
        pass