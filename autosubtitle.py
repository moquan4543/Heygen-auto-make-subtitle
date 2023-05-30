import pyautogui as pg
import time
import os.path
import re
import pyperclip
from PIL import Image


MONITORSIZE = pg.size()

ADDSPEECH = Image.open(os.path.abspath("./src/addspeech.png"))
PLAYBUTTON = Image.open(os.path.abspath("./src/playbutton.png"))
TEXTSCRIPT = Image.open(os.path.abspath("./src/textscript.png"))
TIMELINE = Image.open(os.path.abspath("./src/timeline.png"))
CONTROLLER = Image.open(os.path.abspath("./src/zoomcontroller.png"))
EP = Image.open(os.path.abspath("./src/EP.png"))


def addInitText():
    X = 0
    Y = 0
    while True:
        try:
            X ,Y = pg.center(pg.locateOnScreen(ADDSPEECH,confidence=0.9))
            pg.moveTo(X,Y)
            pg.click()
            print("add speech success!")
            break
        except:
            if(flag):
                time.sleep(0.5)
            else:
                print("Skip the add speech section")
                break
        

def addNewText(text,flag):
    X = 0
    Y = 0
    while True:
        if(flag):
            try:
                X, Y = pg.center(pg.locateOnScreen(TEXTSCRIPT,region=(470,544,400,300),confidence=0.8))
                pg.moveTo(X+50,Y+50)
                pg.click(button="left")
                pg.hotkey("ctrl","a")
                pg.press("delete")
                pyperclip.copy(text)
                pg.hotkey("ctrl","v")
                pg.press("enter")
                print("Text added!(new page)")
                break
            except:
                try:
                    X, Y = pg.center(pg.locateOnScreen(PLAYBUTTON,region=(470,544,300,200)))
                    pg.moveTo(X+50,Y)
                    pg.click(button="left")
                    pg.hotkey("ctrl","a")
                    pg.press("delete")
                    pyperclip.copy(text)
                    pg.hotkey("ctrl","v")
                    pg.press("enter")
                    print("Text added!(new page)")
                    break
                except:
                    try:
                        X, Y = pg.center(pg.locateOnScreen(EP,region=(460,544,310,200)))
                        pg.moveTo(X+50,Y)
                        pg.click(button="left")
                        pg.hotkey("ctrl","a")
                        pg.press("delete")
                        pyperclip.copy(text)
                        pg.hotkey("ctrl","v")
                        pg.press("enter")
                        print("Text added!(new page)")
                        break
                    except:
                        print("The position is not found!")
                        time.sleep(1)
        else:
            try:
                pyperclip.copy(text)
                pg.hotkey("ctrl","v")
                pg.press("enter")
                print("Text added!")
                break
            except:
                print("Error: can't paste the text")
                time.sleep(1)
def Next():
    X = 0
    Y = 0
    X2 = 0
    Y2 = 0
    i = 0
    while True:
        try:
            X, Y = pg.center(pg.locateOnScreen(TIMELINE,confidence=0.8,region=(482,829,1450,100)))
            pg.moveTo(X,Y)
            pg.mouseDown(button="left")
            pg.move(30,0)
            pg.mouseUp(button="left")
            if(pg.locateOnScreen(ADDSPEECH,confidence=0.8,region=(490,536,1100,500)) != None):
                break
        except:
            try:
                value = 300
                if(i >= 5 and i < 9):
                    value += 600
                elif(i >= 9 and i < 14):
                    value -= 700
                elif(i >= 14 and i <19):
                    value += 800
                elif(i >= 19):
                    print("Error: Can't slide")
                    exit()
                X2, Y2 = pg.center(pg.locateOnScreen(CONTROLLER,confidence=0.8,region=(0, MONITORSIZE[1]-200,MONITORSIZE[0],199)))
                pg.moveTo(X2-value,Y2)
                pg.mouseDown(button="left")
                pg.move(20,0)
                pg.mouseUp(button="left")
                i = i + 1
                continue
            except:
                print("Timeline has not found!")
                time.sleep(0.8)

if(__name__ == '__main__'):
    i = 0
    time.sleep(1)
    while True:
        # 指定檔案路徑
        file_path = ''
        print("Please enter the path to txt file:")
        file_path = input()
        if(os.path.exists(file_path)):
            innerflag = True
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # 移除換行符號
                    line = line.strip()
                    if(re.match('^a{10,50}',line) != None):
                        Next()
                        i += 1
                        addInitText()
                        innerflag = True
                        continue
                    time.sleep(0.1)
                    addNewText(line,innerflag)
                    innerflag = False
            print("Done!")
            break
        else:
            print("The file does not exist or the path is wrong, please try again.")