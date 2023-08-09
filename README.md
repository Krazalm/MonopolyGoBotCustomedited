# Monopoly Go! Bot

**Automate gameplay in the Monopoly Go! online game using this Python bot with image recognition capabilities.**

[DEMO](https://youtu.be/-MjjCc4hriI)



## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Disclaimer](#disclaimer)
- [Credits](#credits)
- [Differences](#differences)
- [ChangeLog](#changeLog)

## Features

- Toggle bot operation using a designated toggle key (default: F2).
- Automatically scan and interact with predefined in-game elements.
- Utilizes PyScreeze and PyAutoGUI for image recognition and interaction.
- mainV2.py Customizable keybind functionality for toggling the bot on and off. Support for inputting any character as the toggle key.


## Usage

1. **Clone or Download:**
   Clone or download this repository to your local machine.

2. **Install Dependencies:**
   Install the required Python libraries if not already installed:

   ```sh
   pip install pynput pyautogui pillow pyscreeze opencv-python
   ```
Prepare Screenshots:
Place screenshots of the game elements in the images folder.

Configure:
Adjust configurable parameters in the script, if needed (e.g., DELAY, CONFIDENCE, TOGGLE_KEY).

Run the Bot:
Open a terminal and navigate to the repository folder. Run the script:

 ```sh
python main.py
```
Toggle Bot:
Press the toggle key (F2) to start or stop the bot.

## Configuration
DELAY: The delay (in seconds) between bot cycles.
CONFIDENCE: The confidence level for image recognition.
TOGGLE_KEY: The key used to start and stop the bot (default: F2).

## Disclaimer:
Use responsibly. Please be aware that automating gameplay using this bot may violate the terms of service of the game. This bot is intended for educational and personal use. The developer of this bot assumes no responsibility for any consequences arising from its usage.



## Credits:
This project is based on the original work by Lewis Gibson. We express our gratitude for their contribution. 
https://github.com/lewisgibson
https://github.com/lewisgibson/monopoly-go-bot




## Differences from the original work by Lewis Gibson:

- Implements a class named `MonopolyBot`.
- Uses a continuous loop to process images only when the bot is running.
- Toggles the bot's running status using a specified key (F2) and `pynput.keyboard`.
- Utilizes structured logging to print status messages.
- Obtains sorted image files using a method for image searching.
- Processes images only when the bot is running.
- Uses a class-wide cache for loaded images.
- Offers a more organized and modular design for enhanced maintainability.

## ChangeLog

All notable changes to this project will be documented in this file.

### Added
mainV2.py
- Customizable keybind functionality for toggling the bot on and off.
- Support for inputting any character as the toggle key.

### Changed
- Improved user input validation for toggle key.

## [1.0.0] - 2023-08-09
