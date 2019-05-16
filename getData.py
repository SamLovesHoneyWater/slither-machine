import numpy as np
from PIL import ImageGrab
import cv2
import time,math,os
import win32gui, win32ui, win32con, win32api    # win32 libs

file_iter = 0
uuid = -1

def f(x,y):
    if x == 0:
        return math.copysign(0.25,y)
    if y == 0:
        return 0.25-math.copysign(0.25,x)
    z = math.atan(y/x)
    z = z/math.pi/2
    if x<0 and y>0:
        z = 0.5+z
    elif x<0 and y<0:
        z = z-0.5
    return z

def cord2alpha(cords):
    x,y = cords[0],cords[1]
    x = x-288
    y = -y+476
    alpha = f(x,y)
    if alpha<0:
        alpha = 1+alpha
    return alpha

def is_window(name):
    title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if title == name: return True

def is_slither():
    return is_window('slither.io - Google Chrome')

def fast():
    win32api.keybd_event(32,0,0,0) #32 is spacebar
def slow():
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)  

def process_img(original_image):
    processed = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    #processed = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    #processed = cv2.Canny(processed,threshold1 = 170,threshold2=300)
    return processed
def save_y(n,img,mouse,acc):
    file_name = str(uuid)+'.'+str(n)
    mouse_array = np.array(mouse)
    acc_array = np.array(acc)
    np.save('grayData\\x\\'+file_name,img)
    np.save('grayData\\y1\\'+file_name,mouse_array)
    np.save('grayData\\y2\\'+file_name,acc_array)

def replay(that_uuid):
    try:
        i=0
        while(True):
                time.sleep(0.01)
                shot = np.load('grayData//x//'+str(that_uuid)+'.'+str(i)+'.npy')
                cv2.imshow('window',shot)
                bear = np.load('grayData//y1//'+str(that_uuid)+'.'+str(i)+'.npy')
                print(bear)
                i += 1
                if cv2.waitKey(25)&0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
    except:
        return

uuid_init = 0
if uuid==-1:
    while os.path.exists('grayData//x//'+str(uuid_init)+'.0.npy'):
        uuid_init += 1
    uuid = uuid_init

#main body
replay(0)
last_time = time.time()
while(True):
    while(win32api.GetKeyState(0x43)<0) and is_slither():
        time.sleep(1/60)
        screen = np.array(ImageGrab.grab(bbox=(0,85,576,863))) #576*778=448128
        new_screen = process_img(screen)
        last_time = time.time()

        mouse_pos = win32gui.GetCursorPos()
        if win32api.GetKeyState(0x01)>=0:
            acc = 0
        else:
            acc = 1
        if uuid >= 0:
            save_y(file_iter,new_screen,np.array(cord2alpha(mouse_pos)),acc)
            file_iter = file_iter + 1
        print(file_iter)
        cv2.imshow('window',new_screen)
        if cv2.waitKey(25)&0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

