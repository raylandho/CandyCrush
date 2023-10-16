import pygame
from constants import window_size, CELL_SIZE, ROWS, COLS
from board import Board

pygame.init()
screen = pygame.display.set_mode(window_size)
board = Board()

# Main game loop
running = True
selected_tile = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = (mouse_x - board.x) // min(CELL_SIZE)
            row = (mouse_y - board.y) // min(CELL_SIZE)
            if 0 <= row < ROWS and 0 <= col < COLS:
                if selected_tile is None:
                    selected_tile = (row, col)
                else:
                    # Try to swap the selected tile with the clicked tile
                    board.swap_candies(selected_tile[0], selected_tile[1], row, col)
                    selected_tile = None

    # Handle game logic (checking matches, updating board, etc.)
    board.check_matches()  # Implement this method in board.py
    board.update_board()   # Implement this method in board.py

    # Draw the game board with the selected tile highlighted
    screen.fill((255, 255, 255))
    board.draw_board(screen, selected_tile)
    pygame.display.flip()

pygame.quit()
