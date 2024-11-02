#!/usr/bin/env python3
"""
Classic Snake Game for Python Console
Use arrow keys to control the snake
"""

import os
import sys
import time
import random
import threading
from collections import deque

try:
    import msvcrt  # For Windows
except ImportError:
    import select  # For Unix/Linux/Mac
    import termios
    import tty


class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.score = 0
        self.game_over = False
        self.direction = 'RIGHT'
        self.last_direction = 'RIGHT'
        
        # Initialize snake in the middle of the board
        start_x = width // 2
        start_y = height // 2
        self.snake = deque([(start_x, start_y), (start_x-1, start_y), (start_x-2, start_y)])
        
        # Place first food
        self.food = self._place_food()
        
        # Keyboard input setup
        self.key_pressed = None
        self._setup_keyboard()

    def _setup_keyboard(self):
        """Setup keyboard input for different operating systems"""
        if os.name == 'nt':  # Windows
            self.get_key = self._get_key_windows
        else:  # Unix/Linux/Mac
            self._old_settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin.fileno())
            self.get_key = self._get_key_unix

    def _get_key_windows(self):
        """Get keyboard input for Windows"""
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Arrow keys
                key = msvcrt.getch()
                return key
            return key
        return None

    def _get_key_unix(self):
        """Get keyboard input for Unix/Linux/Mac"""
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return sys.stdin.read(1)
        return None

    def _cleanup_keyboard(self):
        """Clean up keyboard settings"""
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._old_settings)

    def _place_food(self):
        """Place food at random position not occupied by snake"""
        while True:
            food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            if food not in self.snake:
                return food

    def _clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        """Draw the game board"""
        board = []
        
        # Top border
        board.append('┌' + '─' * (self.width * 2) + '┐')
        
        # Game area
        for y in range(self.height):
            row = ['│']
            for x in range(self.width):
                if (x, y) == self.snake[0]:  # Snake head
                    row.append('██')
                elif (x, y) in self.snake:  # Snake body
                    row.append('░░')
                elif (x, y) == self.food:  # Food
                    row.append('◉◉')
                else:  # Empty space
                    row.append('  ')
            row.append('│')
            board.append(''.join(row))
        
        # Bottom border
        board.append('└' + '─' * (self.width * 2) + '┘')
        
        # Score
        board.append(f"Score: {self.score}")
        board.append("Use arrow keys to control. Press 'q' to quit.")
        
        return '\n'.join(board)

    def _process_input(self):
        """Process keyboard input"""
        key = self.get_key()
        
        if key:
            if os.name == 'nt':  # Windows
                if key == b'H':  # Up arrow
                    self.direction = 'UP'
                elif key == b'P':  # Down arrow
                    self.direction = 'DOWN'
                elif key == b'K':  # Left arrow
                    self.direction = 'LEFT'
                elif key == b'M':  # Right arrow
                    self.direction = 'RIGHT'
                elif key == b'q':
                    self.game_over = True
            else:  # Unix/Linux/Mac
                if key == '\x1b':  # Escape sequence for arrow keys
                    # Read the next two characters
                    key = sys.stdin.read(2)
                    if key == '[A':
                        self.direction = 'UP'
                    elif key == '[B':
                        self.direction = 'DOWN'
                    elif key == '[C':
                        self.direction = 'RIGHT'
                    elif key == '[D':
                        self.direction = 'LEFT'
                elif key == 'q':
                    self.game_over = True

    def _update_game(self):
        """Update game state"""
        # Prevent 180-degree turns
        if (self.direction == 'UP' and self.last_direction == 'DOWN') or \
           (self.direction == 'DOWN' and self.last_direction == 'UP') or \
           (self.direction == 'LEFT' and self.last_direction == 'RIGHT') or \
           (self.direction == 'RIGHT' and self.last_direction == 'LEFT'):
            self.direction = self.last_direction

        head_x, head_y = self.snake[0]
        
        # Calculate new head position
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        
        # Check for collisions with walls
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.game_over = True
            return
        
        # Check for collisions with self
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Move snake
        self.snake.appendleft(new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self._place_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
        
        self.last_direction = self.direction

    def run(self):
        """Main game loop"""
        try:
            while not self.game_over:
                self._clear_screen()
                print(self._draw_board())
                
                self._process_input()
                self._update_game()
                
                time.sleep(0.1)  # Game speed
            
            # Game over screen
            self._clear_screen()
            print("GAME OVER!")
            print(f"Final Score: {self.score}")
            print("Thanks for playing!")
            
        finally:
            self._cleanup_keyboard()


def main():
    """Main function to start the game"""
    print("Welcome to Snake Game!")
    print("Controls: Arrow keys to move, 'q' to quit")
    print("Press Enter to start...")
    input()
    
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()