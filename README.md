# Snake Game - Python Console Implementation

## Overview
A classic Snake game implemented in Python that runs in the console/terminal with keyboard controls.

## Files Structure
- `snake_game.py` - Main game launcher
- `game_engine.py` - Core game logic and rendering
- `requirements.txt` - Dependency information

## Requirements
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation & Usage

1. **Save all files** in the same directory

2. **Run the game**:
   ```bash
   python snake_game.py
   ```

3. **Game Controls**:
   - **W** - Move Up
   - **S** - Move Down  
   - **A** - Move Left
   - **D** - Move Right
   - **Q** - Quit Game

## Game Features
- Snake grows when eating food (★)
- Score tracking
- Wall collision detection
- Self-collision detection
- Real-time keyboard controls
- Cross-platform compatibility (Windows/Linux/macOS)

## How to Play
1. Run the game using `python snake_game.py`
2. Press Enter to start
3. Use WASD keys to control the snake
4. Eat the food (★) to grow and increase score
5. Avoid hitting walls or yourself
6. Press Q to quit anytime

## Platform Notes
- **Windows**: Uses `msvcrt` for keyboard input
- **Unix/Linux/macOS**: Uses `select` for non-blocking input

## Customization
You can modify these parameters in `game_engine.py`:
- `width` and `height`: Game board dimensions
- Game speed: Adjust the `time.sleep()` value in the `run()` method

Enjoy the game!