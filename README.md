# Slither machine

This is an improvised AI for the game Slither. 
I'm kinda new to this, so if there are any mistakes or inefficiencies in my code please do point them out. I would appreciate suggestions greatly :)

1) To collect your own data, create a folder named "grayData" in the same directory where the python files are. In "grayData", create three folders named "x", "y1", and "y2". In Windows 10, set your screen resolution to 1152*864. Open Slither(slither.io) in your Internet explorer and drag and move the window to the far left of your screen so that it appears on the left half of the screen(Windows should automatically split the screen in half for you). While you play the game, press and hold "c" on your keyboard, and your actions will be stored with the corresponding screenshots. They will be stored as numpy files in the data folders.

2) To train your model, run "train conv.py" and specify the name of the file where your model will be stored.

3) To use your model, specify the name of the model file before running "use.py". Configure your game window as you did in "1)". Press and hold "c" during the game to let your model take control.

# Currently, only the bearing of the snake is considered. There is no classification model to determine whether to boost speed or not, but the speeding data are stored anyways, just in case of future work. Note that they are not stored one-hot, but as binaries.