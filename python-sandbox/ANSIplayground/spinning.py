import time, sys
from datetime import datetime 

def spinning(stop=50):
    t1 = datetime.now()
    spin = ['-','\\','|', '/']
    index = 0
    sys.stdout.write(u"\u001b[?25l") # Hide cursor
    while (datetime.now()-t1).seconds <= stop:
        index = index+1 if index < len(spin)-1 else 0
        sys.stdout.write(u"\u001b[1000D" + spin[index]) # Spiiiiiiiiiiiiiin
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(u"\u001b[?25h") # Show cursor

spinning(2.5)