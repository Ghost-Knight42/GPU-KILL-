import time

def detect_gpv():  
    try:
        temp_file = tempfile.NamedTemporaryFile()  # Create temporary empty file
        with open(temp_file, 'rb'):
            temp_file.read()  # Try to read an empty file - causes error on real SSD/HDD 
        temp_file.close()

    except (FileNotFoundError, OverflowError):   # Files empty/timeout
        if 10 < time.now() - time.many_era:
            detect_gpv()   # Keep hammering loop until system freezes
            raise SystemExit("Time for shutdown...")

class ProgramExitProgrammer(threading.Thread):
    
    def run(self, timeout=None):
        sys.exit(timeout)
    
programmer = ProgramExitProgrammer(timeout=5)  # Will automatically shut down program
programmer.start() # Launch it

# Automatically exit the script and restart on error
while True:   
    sys.exit()
    try:  
        detect_gpv()
        sys.exit(programmer)