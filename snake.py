"""
Snake class that handles snake movement and growth
"""
import sys
import select
import tty
import termios

class Snake:
    def __init__(self, start_x, start_y):
        self.body = [(start_x, start_y)]
        self.direction = (1, 0)  # Start moving right
        self.growth_pending = 0
        
    def get_head(self):
        """Get the position of the snake's head"""
        return self.body[0]
    
    def move(self):
        """Move the snake in the current direction"""
        self._handle_input()
        
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            self.body.pop()
    
    def grow(self):
        """Make the snake grow by one segment"""
        self.growth_pending += 1
    
    def change_direction(self, new_direction):
        """Change the snake's direction if valid"""
        # Prevent 180-degree turns
        current_dx, current_dy = self.direction
        new_dx, new_dy = new_direction
        
        if (current_dx + new_dx != 0) or (current_dy + new_dy != 0):
            self.direction = new_direction
    
    def check_self_collision(self):
        """Check if snake has collided with itself"""
        head = self.body[0]
        return head in self.body[1:]
    
    def _handle_input(self):
        """Handle keyboard input for direction changes"""
        # Non-blocking input check
        if self._kbhit():
            key = sys.stdin.read(1).lower()
            
            if key == 'w':  # Up
                self.change_direction((0, -1))
            elif key == 's':  # Down
                self.change_direction((0, 1))
            elif key == 'a':  # Left
                self.change_direction((-1, 0))
            elif key == 'd':  # Right
                self.change_direction((1, 0))
            elif key == 'q':  # Quit
                print("\nGame quit by user!")
                sys.exit(0)
    
    def _kbhit(self):
        """Check if a key has been pressed (non-blocking)"""
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])