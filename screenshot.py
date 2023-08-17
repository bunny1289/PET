import keyboard
import time
from PIL import ImageGrab
import uploadmongo
def take_screenshot():
    # Get the current time for naming the screenshot
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Capture the screenshot
    screenshot = ImageGrab.grab()
    
    # Save the screenshot
    screenshot.save(f"screenshot_{timestamp}.png")
    print(f"Screenshot saved as screenshot_{timestamp}.png")
    uploadmongo.trigger()

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

if __name__ == "__main__":
    main()
