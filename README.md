## Snake Game - Python Console Version

A classic Snake game implemented in Python that runs in the console with keyboard controls.

### Features
- 🐍 Classic Snake gameplay
- 🎮 Keyboard controls (WASD or Arrow Keys)
- 🍎 Food collection and score tracking
- 🎯 Collision detection (walls and self)
- 📊 Score display
- 🖥️ Cross-platform compatibility

### Requirements
- Python 3.6 or higher
- No external dependencies required!

### How to Run

1. **Make sure you have all files in the same directory:**
   - `snake_game.py` (main game logic)
   - `game_utils.py` (utility functions)
   - `run_game.py` (launcher script)
   - `requirements.txt` (dependencies info)

2. **Run the game using one of these methods:**

   **Method 1: Using the launcher script**
   ```bash
   python run_game.py
   ```

   **Method 2: Direct execution**
   ```bash
   python snake_game.py
   ```

### Controls
- **W** or **↑** - Move Up
- **S** or **↓** - Move Down  
- **A** or **←** - Move Left
- **D** or **→** - Move Right
- **Q** - Quit Game

### Game Rules
1. Control the snake to eat the food (🍎)
2. Each food eaten increases your score by 10 points
3. The snake grows longer with each food eaten
4. Game ends if you:
   - Hit the wall
   - Collide with yourself
   - Press 'Q' to quit

### Troubleshooting
- If arrow keys don't work, use WASD keys instead
- On Windows, the game uses `msvcrt` for input
- On Unix/Linux/Mac, it uses `termios` and `select`
- Make sure your terminal window is large enough to display the game board

Enjoy the game! 🎮