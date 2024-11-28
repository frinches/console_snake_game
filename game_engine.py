"""
Game engine that handles the main game loop and logic
"""
import time
import sys
from snake import Snake
from food import Food
from game_board import GameBoard

class GameEngine:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = Snake(width // 2, height // 2)
        self.food = Food(width, height)
        self.board = GameBoard(width, height)
        self.score = 0
        self.game_over = False
        
    def run(self):
        """Main game loop"""
        while not self.game_over:
            # Update game state
            self._update()
            
            # Render the game
            self._render()
            
            # Control game speed
            time.sleep(0.2)
            
        self._game_over_screen()
    
    def _update(self):
        """Update game state"""
        # Move snake
        self.snake.move()
        
        # Check for collisions with walls
        head = self.snake.get_head()
        if (head[0] < 0 or head[0] >= self.width or 
            head[1] < 0 or head[1] >= self.height):
            self.game_over = True
            return
        
        # Check for collisions with self
        if self.snake.check_self_collision():
            self.game_over = True
            return
        
        # Check for food collision
        if head == self.food.position:
            self.snake.grow()
            self.food.respawn(self.width, self.height, self.snake.body)
            self.score += 10
    
    def _render(self):
        """Render the game state"""
        # Clear console (works on most systems)
        print("\033[H\033[J", end="")
        
        # Update board
        self.board.update(self.snake.body, self.food.position)
        
        # Display game info
        print(f"Score: {self.score}")
        print(f"Snake Length: {len(self.snake.body)}")
        print()
        
        # Display the board
        self.board.display()
        
        # Display controls reminder
        print("\nControls: W (Up), S (Down), A (Left), D (Right), Q (Quit)")
    
    def _game_over_screen(self):
        """Display game over screen"""
        print("\n" + "="*30)
        print("GAME OVER!")
        print(f"Final Score: {self.score}")
        print(f"Snake Length: {len(self.snake.body)}")
        print("="*30)
        input("Press Enter to exit...")