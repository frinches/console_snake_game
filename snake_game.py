#!/usr/bin/env python3
"""
Classic Snake Game for Python Console
Controls: W (up), S (down), A (left), D (right), Q (quit)
"""

import os
import sys
import time
import random
import threading
from game_engine import GameEngine

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main game function"""
    print("Welcome to Snake Game!")
    print("Controls: W (up), S (down), A (left), D (right), Q (quit)")
    print("Press Enter to start...")
    input()
    
    game = GameEngine()
    
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
    print(f"Final Score: {game.score}")

if __name__ == "__main__":
    main()