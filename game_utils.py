import os
import sys

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key(timeout=0):
    """Get a single key press from user with optional timeout"""
    try:
        if sys.platform.startswith('win'):
            # Windows implementation
            import msvcrt
            import time
            
            start_time = time.time()
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    return key
                
                if timeout > 0 and (time.time() - start_time) >= timeout:
                    return None
                
                time.sleep(0.01)
        else:
            # Unix/Linux implementation
            import select
            import termios
            import tty
            
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            
            try:
                tty.setraw(fd)
                if timeout > 0:
                    # With timeout
                    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
                    if rlist:
                        key = sys.stdin.read(1).lower()
                        return key
                    else:
                        return None
                else:
                    # Without timeout (blocking)
                    key = sys.stdin.read(1).lower()
                    return key
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                
    except Exception as e:
        # Fallback implementation
        if timeout > 0:
            import time
            time.sleep(timeout)
        return None