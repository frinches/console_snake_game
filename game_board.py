"""
Game board class that handles rendering the game state
"""

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    def update(self, snake_body, food_position):
        """Update the board with current snake and food positions"""
        # Clear the grid
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Place food
        food_x, food_y = food_position
        self.grid[food_y][food_x] = '●'
        
        # Place snake
        for i, (x, y) in enumerate(snake_body):
            if i == 0:  # Snake head
                self.grid[y][x] = '■'
            else:  # Snake body
                self.grid[y][x] = '□'
    
    def display(self):
        """Display the current game board"""
        # Top border
        print('┌' + '─' * (self.width * 2 - 1) + '┐')
        
        # Game area
        for row in self.grid:
            print('│' + ' '.join(row) + '│')
        
        # Bottom border
        print('└' + '─' * (self.width * 2 - 1) + '┘')