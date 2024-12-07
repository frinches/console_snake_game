"""
Food class that handles food generation and placement
"""
import random

class Food:
    def __init__(self, board_width, board_height):
        self.position = (0, 0)
        self.respawn(board_width, board_height, [])
    
    def respawn(self, board_width, board_height, snake_body):
        """Place food in a random position not occupied by the snake"""
        while True:
            x = random.randint(0, board_width - 1)
            y = random.randint(0, board_height - 1)
            new_position = (x, y)
            
            # Make sure food doesn't spawn on snake
            if new_position not in snake_body:
                self.position = new_position
                break