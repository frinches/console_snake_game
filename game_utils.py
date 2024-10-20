"""
Utility functions for the Snake game
Handles cross-platform screen clearing and keyboard input
"""

import os
import sys
import select
import termios
import tty

def clear_screen():
    """Clear the console screen (cross-platform)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key(timeout=0.1):
    """
    Get a single key press with timeout
    Returns the key pressed or empty string if timeout
    """
    if sys.platform.startswith('win'):
        # Windows implementation
        import msvcrt
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            return key
        return ''
    else:
        # Unix/Linux/Mac implementation
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            if rlist:
                key = sys.stdin.read(1)
                # Handle arrow keys (multi-character sequences)
                if key == '\x1b':
                    # Escape sequence for arrow keys
                    key2 = sys.stdin.read(1)
                    key3 = sys.stdin.read(1)
                    if key2 == '[':
                        if key3 == 'A':
                            return 'UP'
                        elif key3 == 'B':
                            return 'DOWN'
                        elif key3 == 'C':
                            return 'RIGHT'
                        elif key3 == 'D':
                            return 'LEFT'
                return key
            return ''
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def setup_terminal():
    """Setup terminal for proper game display"""
    if not sys.platform.startswith('win'):
        # Set terminal to raw mode for better input handling
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        return old_settings
    return None

def restore_terminal(old_settings):
    """Restore terminal settings"""
    if old_settings and not sys.platform.startswith('win'):
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)