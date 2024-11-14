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
        self.direction = (0, 1)  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        
    def generate_food(self):
        """Generate food at random position not occupied by snake"""
        while True:
            food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if food not in self.snake:
                return food
    
    def change_direction(self, key):
        """Change snake direction based on keyboard input"""
        if key == 'w' and self.direction != (1, 0):  # Up
            self.direction = (-1, 0)
        elif key == 's' and self.direction != (-1, 0):  # Down
            self.direction = (1, 0)
        elif key == 'a' and self.direction != (0, 1):  # Left
            self.direction = (0, -1)
        elif key == 'd' and self.direction != (0, -1):  # Right
            self.direction = (0, 1)
    
    def move_snake(self):
        """Move snake one step in current direction"""
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Check for collision with walls
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width):
            self.game_over = True
            return
        
        # Check for collision with self
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Move snake
        self.snake.insert(0, new_head)
        
        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
    
    def draw(self):
        """Draw the game board"""
        clear_screen()
        print(f"Score: {self.score}")
        print("+" + "-" * self.width + "+")
        
        for row in range(self.height):
            line = "|"
            for col in range(self.width):
                pos = (row, col)
                if pos == self.snake[0]:  # Snake head
                    line += "O"
                elif pos in self.snake:  # Snake body
                    line += "o"
                elif pos == self.food:  # Food
                    line += "*"
                else:  # Empty space
                    line += " "
            line += "|"
            print(line)
        
        print("+" + "-" * self.width + "+")
        print("Controls: W=Up, A=Left, S=Down, D=Right, Q=Quit")
    
    def run(self):
        """Main game loop"""
        while not self.game_over:
            self.draw()
            
            # Get user input with timeout
            key = get_key(0.2)
            
            if key == 'q':
                print("\nGame quit!")
                break
            
            if key:
                self.change_direction(key)
            
            self.move_snake()
            time.sleep(0.1)
        
        if self.game_over:
            self.draw()
            print(f"\nGame Over! Final Score: {self.score}")

def main():
    print("Welcome to Snake Game!")
    print("Use W, A, S, D keys to control the snake.")
    print("Press any key to start...")
    get_key()
    
    game = SnakeGame()
    game.run()

if __name__ == "__main__":
    main()