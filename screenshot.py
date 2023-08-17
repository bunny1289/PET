import keyboard
import time
from PIL import ImageGrab
import uploadmongo
import threading
# thread2 = threading.Thread(target=uploadmongo.trigger)
threads = []
def take_screenshot():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot_{timestamp}.png")
    print(f"Screenshot saved as screenshot_{timestamp}.png")
    uploadmongo.trigger('coding')

def new_thread():
    thread = threading.Thread(target=take_screenshot)
    threads.append(thread)
    thread.start()
    

def main():

    print("Press a + S to take a screenshot.")
    

    # Listen for the Ctrl + Shift + S combination
    keyboard.add_hotkey("a+s", take_screenshot)
    
    try:
        keyboard.wait("esc")  # Wait for the 'esc' key to exit the program
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.remove_hotkey("a+s")  # Remove the hotkey listener

        

# thread1 = threading.Thread(target=take_screenshot)


if __name__ == "__main__":
    main()
