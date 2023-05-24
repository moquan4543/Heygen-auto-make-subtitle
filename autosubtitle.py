'''
流程:
1.剪映輸出字幕選txt檔
2.可以利用馴碼快手轉成繁體中文(option)
3.手動根據老師講的內容分好哪幾句話是同一頁PPT中講的，不同頁的內容用連續10至50個字母'a'來分隔
4.將改好的txt檔讀入這隻程式裡(在main中指定好路徑)
5.手動將進度條拉至第一張投影片，注意需要有add speech字樣
6.執行程式
'''
import pyautogui as pg
import time
import os.path
import re
import pyperclip
from PIL import Image


MONITORSIZE = pg.size()

ADDSPEECH = Image.open(os.path.abspath("./automakevideo/addspeech.png"))
PLAYBUTTON = Image.open(os.path.abspath("./automakevideo/playbutton.png"))
TEXTSCRIPT = Image.open(os.path.abspath("./automakevideo/textscript.png"))
TIMELINE = Image.open(os.path.abspath("./automakevideo/timeline.png"))
CONTROLLER = Image.open(os.path.abspath("./automakevideo/zoomcontroller.png"))
DEFAULTVOICE = Image.open(os.path.abspath("./automakevideo/defaultvoice.png"))
FILTLANG = Image.open(os.path.abspath("./automakevideo/filtbylang.png"))
FILTCHINESE = Image.open(os.path.abspath("./automakevideo/filtchinese.png"))
TARGETVOICE = Image.open(os.path.abspath("./automakevideo/voicetarget.png"))
SELECTVOICE = Image.open(os.path.abspath("./automakevideo/selectvoice.png"))
SPEED = Image.open(os.path.abspath("./automakevideo/speed.png"))
EP = Image.open(os.path.abspath("./automakevideo/EP.png"))





def addInitText(flag):
    X = 0
    Y = 0
    while True:
        try:
            X ,Y = pg.center(pg.locateOnScreen(ADDSPEECH,confidence=0.9))
            pg.moveTo(X,Y)
            pg.click()
            print("add speech success!")
            if(flag):
                pg.move(400,-90)
                pg.click()
                time.sleep(1.5)
                X,Y = pg.center(pg.locateOnScreen(FILTLANG))
                pg.moveTo(X,Y)
                time.sleep(0.3)
                pg.click()
                X,Y = pg.center(pg.locateOnScreen(FILTCHINESE,confidence=0.9))
                pg.moveTo(X,Y)
                time.sleep(0.3)
                pg.click()
                pg.move(100,-400)
                X,Y = pg.center(pg.locateOnScreen(TARGETVOICE))
                pg.moveTo(X,Y)
                time.sleep(0.3)
                X,Y = pg.center(pg.locateOnScreen(SELECTVOICE))
                pg.moveTo(X,Y)
                time.sleep(0.3)
                pg.click()
            print("select voice success!")
            time.sleep(0.8)
            pg.moveTo(1779,716)
            time.sleep(0.2)
            pg.mouseDown(button="left")
            pg.moveTo(1744,716,0.1)
            pg.mouseUp(button="left")
            print("modify speed success!")
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
                if(i >= 5):
                    value += 600
                elif(i >= 9):
                    value -= 700
                elif(i >= 14):
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
    flag = True
    i = 0
    time.sleep(1)
    # 指定檔案路徑
    file_path = 'C:/build/subtitle.txt'
    addInitText(flag)
    flag = False
    innerflag = True
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 移除換行符號
            line = line.strip()
            if(re.match('^a{10,50}',line) != None):
                Next()
                i += 1
                addInitText(flag)
                innerflag = True
                continue
            time.sleep(0.5)
            addNewText(line,innerflag)
            innerflag = False