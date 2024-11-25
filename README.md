## Snake Game - Console Version

A simple implementation of the classic Snake game that runs in the Python console with keyboard controls.

### How to Use

1. **Requirements**: 
   - Python 3.6 or higher
   - No external dependencies required

2. **Running the Game**:
   ```bash
   python snake_game.py
   ```

3. **Controls**:
   - **W**: Move Up
   - **A**: Move Left  
   - **S**: Move Down
   - **D**: Move Right
   - **Q**: Quit Game

4. **Game Rules**:
   - Control the snake (O = head, o = body) to eat the food (*)
   - Each food eaten increases your score by 10 points
   - The snake grows longer with each food eaten
   - Game ends if the snake hits the wall or itself

5. **Files Description**:
   - `snake_game.py`: Main game logic and entry point
   - `game_utils.py`: Utility functions for screen clearing and keyboard input
   - `requirements.txt`: Dependency information (none required)

### Features
- Real-time keyboard controls
- Score tracking
- Game over detection (wall collision, self collision)
- Cross-platform compatibility (Windows, Linux, macOS)

### Troubleshooting
- If keyboard input doesn't work properly, try running in a different terminal/console
- On some systems, you may need to press Enter after certain keys
- The game uses non-blocking input with timeout for smooth gameplay

Enjoy the game!