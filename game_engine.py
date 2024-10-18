import threading
import time
import sys
import select

class GameEngine:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]
        self.direction = (0, 1)  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.last_key = None
        
    def generate_food(self):
        """Generate food at random position not occupied by snake"""
        while True:
            food_pos = (random.randint(0, self.height - 1), 
                       random.randint(0, self.width - 1))
            if food_pos not in self.snake:
                return food_pos
    
    def get_keyboard_input(self):
        """Non-blocking keyboard input reader"""
        while not self.game_over:
            if sys.platform == 'win32':
                # Windows implementation
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    self.last_key = key
            else:
                # Unix implementation
                if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                    key = sys.stdin.read(1).lower()
                    self.last_key = key
            time.sleep(0.1)
    
    def process_input(self):
        """Process the last keyboard input"""
        if not self.last_key:
            return
            
        key = self.last_key
        self.last_key = None
        
        # Update direction based on key press
        if key == 'w' and self.direction != (1, 0):  # Up
            self.direction = (-1, 0)
        elif key == 's' and self.direction != (-1, 0):  # Down
            self.direction = (1, 0)
        elif key == 'a' and self.direction != (0, 1):  # Left
            self.direction = (0, -1)
        elif key == 'd' and self.direction != (0, -1):  # Right
            self.direction = (0, 1)
        elif key == 'q':  # Quit
            self.game_over = True
    
    def update(self):
        """Update game state"""
        # Calculate new head position
        head_row, head_col = self.snake[0]
        dir_row, dir_col = self.direction
        new_head = (head_row + dir_row, head_col + dir_col)
        
        # Check collision with walls
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width):
            self.game_over = True
            return
        
        # Check collision with self
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
    
    def render(self):
        """Render the game state"""
        # Clear screen
        print("\033[2J\033[H", end="")  # ANSI escape codes to clear screen
        
        # Draw border and game area
        print(f"Score: {self.score}")
        print("+" + "-" * self.width + "+")
        
        for row in range(self.height):
            line = "|"
            for col in range(self.width):
                pos = (row, col)
                if pos == self.snake[0]:  # Snake head
                    line += "●"
                elif pos in self.snake:  # Snake body
                    line += "○"
                elif pos == self.food:  # Food
                    line += "★"
                else:  # Empty space
                    line += " "
            line += "|"
            print(line)
        
        print("+" + "-" * self.width + "+")
        print("Controls: W (up), S (down), A (left), D (right), Q (quit)")
    
    def run(self):
        """Main game loop"""
        # Start keyboard input thread
        input_thread = threading.Thread(target=self.get_keyboard_input, daemon=True)
        input_thread.start()
        
        # Game loop
        while not self.game_over:
            self.process_input()
            self.update()
            self.render()
            
            # Game speed (adjust for difficulty)
            time.sleep(0.2)