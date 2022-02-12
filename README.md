# Slither machine

This is an improvised AI for the game Slither.

1) To collect your own data, create a folder named "grayData" in the same directory where the python files are. In "grayData", create three folders named "x", "y1", and "y2". In Windows 10, set your screen resolution to 1152*864. Open Slither(slither.io) in your Internet explorer and drag and move the window to the far left of your screen so that it appears on the left half of the screen (Windows should automatically split the screen in half for you). While you play the game, press and hold "c" on your keyboard, and your actions will be stored with the corresponding screenshots. They will be stored as numpy files in the data folders.

2) To train your model, run "train conv.py" and specify the name of the file where your model will be stored.

3) To use your model, specify the name of the model file before running "use.py". Configure your game window as you did in step one. Press and hold the "c" key during the game to let your model take control. Release "c" to restore manual control.

Note that the model currently only learns through supervised training by immitating the gameplay in its training data. Reinforcement learning is yet to be implemented.

Currently, only the bearing of the snake is considered. There is no classification model to determine whether to boost speed or not, but the speeding data are stored anyways to pave the way for future work. Note that they are not stored as one-hot, but as binaries.
