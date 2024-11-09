## Snake Game - Console Version

A classic Snake game implemented in Python that runs in the terminal/console with keyboard controls.

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

### Installation & Setup

1. **Download the files:**
   - `snake_game.py` (main game file)
   - `requirements.txt` (dependency info)
   - `install.py` (optional setup script)

2. **Run the setup (optional):**
   ```bash
   python install.py
   ```

3. **Start the game:**
   ```bash
   python snake_game.py
   ```

### How to Play

1. **Controls:**
   - **Arrow Keys**: Move the snake (Up/Down/Left/Right)
   - **Q**: Quit the game

2. **Game Rules:**
   - Control the snake (██ head, ░░ body) to eat food (◉◉)
   - Each food eaten increases your score by 10 points
   - The snake grows longer with each food consumed
   - Game ends if you:
     - Hit the wall
     - Collide with yourself
     - Press 'q' to quit

3. **Game Board:**
   ```
   ┌────────────────────────┐
   │                        │
   │        ██░░░░◉◉        │
   │                        │
   └────────────────────────┘
   Score: 30
   Use arrow keys to control. Press 'q' to quit.
   ```

### Features
- Cross-platform compatibility (Windows, Linux, Mac)
- Real-time keyboard input
- Score tracking
- Simple console-based graphics
- No external dependencies

### Troubleshooting

**Windows:**
- Make sure Command Prompt or PowerShell supports arrow keys
- Run as administrator if keyboard input doesn't work

**Linux/Mac:**
- Ensure terminal supports ANSI escape sequences
- Some terminals might require additional configuration for raw input

**Common Issues:**
- If arrow keys don't work, try running in a different terminal
- Game runs too fast/slow? Adjust the `time.sleep(0.1)` value in `snake_game.py`

### File Structure
- `snake_game.py` - Main game implementation
- `requirements.txt` - Dependency information
- `install.py` - Setup and instructions script

Enjoy the classic Snake game! 🐍