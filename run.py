import multiprocessing
import subprocess
import eel

# Initialize Eel
eel.init('web')  # Replace 'web' with your actual folder containing HTML/JS files

# Print registered functions to verify Eel initialization
print("Registered functions (before processes):", eel._exposed_functions.keys())

# Function to run Astrick
def startAstrick():
    print("Process 1 is running.")
    from main import start
    start()

# Function to run hotword listener
def listenHotword():
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    # Start the multiprocessing tasks
    p1 = multiprocessing.Process(target=startAstrick)
    p2 = multiprocessing.Process(target=listenHotword)

    # Start processes
    p1.start()
    subprocess.call([r'device.bat'])
    p2.start()

    # Wait for process 1 to complete
    p1.join()

    # Terminate process 2 if it's still alive
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")
