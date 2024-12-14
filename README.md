# Snake Game - Console Version

## Overview
A classic Snake game implemented in Python that runs in the console with keyboard controls.

## Files Structure
- `snake_game.py` - Main entry point
- `game_engine.py` - Main game loop and logic
- `snake.py` - Snake movement and controls
- `food.py` - Food generation
- `game_board.py` - Game board rendering

## Requirements
- Python 3.6+
- Unix-like terminal (Linux/macOS) or Windows Command Prompt/PowerShell

## How to Run
1. Save all files in the same directory
2. Run the main script:
   ```bash
   python snake_game.py
   ```

## Controls
- **W** - Move Up
- **S** - Move Down  
- **A** - Move Left
- **D** - Move Right
- **Q** - Quit Game

## Game Rules
- Control the snake to eat food (●)
- Each food eaten increases your score by 10 points and makes the snake grow
- Game ends if:
  - Snake hits the wall
  - Snake collides with itself
- Try to achieve the highest score possible!

## Features
- Real-time keyboard input
- Score tracking
- Snake length display
- Visual board with borders
- Collision detection

## Notes
- The game uses non-blocking input for smooth controls
- Board size is configurable (default: 20x15)
- Game speed is fixed at 0.2 seconds per frame

Enjoy the game! 🐍