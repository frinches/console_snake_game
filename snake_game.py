"""
Classic Snake Game for Python Console
Uses keyboard controls for movement
"""

import os
import time
import random
import sys
from game_utils import clear_screen, get_key

class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]
        self.food = self.generate_food()
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        
    def generate_food(self):
        """Generate food at random position not occupied by snake"""
        while True:
            food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if food not in self.snake:
                return food
    
    def draw_board(self):
        """Draw the game board with snake, food, and borders"""
        clear_screen()
        
        # Draw top border
        print('┌' + '─' * (self.width * 2) + '┐')
        
        for row in range(self.height):
            line = '│'
            for col in range(self.width):
                if (row, col) == self.snake[0]:
                    line += '██'  # Snake head
                elif (row, col) in self.snake:
                    line += '░░'  # Snake body
                elif (row, col) == self.food:
                    line += '🍎'  # Food
                else:
                    line += '  '  # Empty space
            line += '│'
            print(line)
        
        # Draw bottom border
        print('└' + '─' * (self.width * 2) + '┘')
        print(f"Score: {self.score} | Use WASD or Arrow Keys to move | Press 'Q' to quit")
    
    def move_snake(self):
        """Move the snake in current direction"""
        head_row, head_col = self.snake[0]
        
        # Calculate new head position based on direction
        if self.direction == 'UP':
            new_head = (head_row - 1, head_col)
        elif self.direction == 'DOWN':
            new_head = (head_row + 1, head_col)
        elif self.direction == 'LEFT':
            new_head = (head_row, head_col - 1)
        elif self.direction == 'RIGHT':
            new_head = (head_row, head_col + 1)
        
        # Check for collisions
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width or
            new_head in self.snake):
            self.game_over = True
            return
        
        # Move snake
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
    
    def change_direction(self, new_direction):
        """Change snake direction (prevent 180-degree turns)"""
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def run(self):
        """Main game loop"""
        print("Welcome to Snake Game!")
        print("Controls: WASD or Arrow Keys to move, Q to quit")
        input("Press Enter to start...")
        
        while not self.game_over:
            self.draw_board()
            
            # Get user input with timeout
            key = get_key(0.2)
            
            if key == 'q' or key == 'Q':
                break
            
            # Handle movement keys
            key_directions = {
                'w': 'UP', 'W': 'UP', 
                's': 'DOWN', 'S': 'DOWN',
                'a': 'LEFT', 'A': 'LEFT',
                'd': 'RIGHT', 'D': 'RIGHT',
                'UP': 'UP', 'DOWN': 'DOWN', 'LEFT': 'LEFT', 'RIGHT': 'RIGHT'
            }
            
            if key in key_directions:
                self.change_direction(key_directions[key])
            
            self.move_snake()
            time.sleep(0.1)  # Game speed
        
        # Game over screen
        clear_screen()
        print("┌─────────────────────────┐")
        print("│      GAME OVER!         │")
        print("└─────────────────────────┘")
        print(f"Final Score: {self.score}")
        print(f"Snake Length: {len(self.snake)}")
        print("\nThanks for playing!")

def main():
    """Main function to start the game"""
    try:
        game = SnakeGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()