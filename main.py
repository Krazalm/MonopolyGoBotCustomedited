import time
import glob
import pyscreeze
import PIL.Image
import pynput
import pyautogui
import logging

# Configurable Parameters
DELAY = 0
CONFIDENCE = 0.75
TOGGLE_KEY = pynput.keyboard.Key.f2 # Don't Change

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MonopolyBot:
    def __init__(self) -> None:
        self.images_path = "images"
        self.cache = {}
        self.running = False

        # Initialize keyboard listener
        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()

        self.print_banner()

        while True:
            if self.running:
                self.process_images()
            time.sleep(DELAY)

    def print_banner(self) -> None:
        print("Monopoly Go! Bot")
        print(f"\nPress {TOGGLE_KEY} to toggle running.\n")

    def on_key_press(self, key) -> None:
        if key == TOGGLE_KEY:
            self.toggle_running()

    def toggle_running(self) -> None:
        self.running = not self.running
        status = "Started" if self.running else "Stopped"
        print(f"{status}\n")
        logger.info(f"Bot {status.lower()}.")

    def process_images(self) -> None:
        for path in self.get_sorted_images():
            if not self.running:
                break
            if self.process_image(path):
                break

    def get_sorted_images(self) -> list:
        return sorted(glob.glob(f"{self.images_path}/*.png"))

    def load_image(self, path: str) -> PIL.Image.Image:
        if path not in self.cache:
            self.cache[path] = PIL.Image.open(path)
        return self.cache[path]

    def find(self, image: PIL.Image.Image) -> pyscreeze.Point | None:
        result = pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=CONFIDENCE)
        return result

    def process_image(self, path: str) -> bool:
        image = self.load_image(path)
        point = self.find(image)

        if point:
            print(f"Scanning for {path} -> ({point.x}, {point.y})")
            pyautogui.click(point)
            logger.info(f"Clicked on {path} at ({point.x}, {point.y}).")
            return True

        print(f"Scanning for {path}")
        return False

def main():
    MonopolyBot()

if __name__ == "__main__":
    main()
