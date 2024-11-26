"""
Main entry point for the Snake Game
"""
from game_engine import GameEngine

def main():
    """Main function to start the Snake game"""
    print("Welcome to Snake Game!")
    print("Controls: W (Up), S (Down), A (Left), D (Right), Q (Quit)")
    print("Press Enter to start...")
    input()
    
    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()