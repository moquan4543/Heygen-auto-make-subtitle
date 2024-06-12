from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import SB
import os
import time

# 讀取處理txt
filePath = ''
while(True):
    print("Please enter the path to txt file:")
    filePath = input()
    if(os.path.exists(filePath)):
        with open(filePath, 'r', encoding='utf-8') as file: 
            content = file.read()
            break
    else:
        print("cant open file, please try again...")
paragraphs = content.split('*\n')

with SB(uc=True) as sb:
    #等待使用者手動登入
    sb.driver.get("https://app.heygen.com/home")
    input("請手動登入Heygen並進入要匯入字幕的draft頁面，完成後按Enter繼續...")

    # 等待並點擊add script
    wait = WebDriverWait(sb.driver, 10)
    try:
        addInitScriptButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[4]/div[2]')))
    except Exception:
        try:
            addInitScriptButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[4]')))
        except Exception:
            print("Something went wrong, please try again\n")
            print(Exception)
            print(Exception.args)
            print(Exception.__cause__)
            print(Exception.__context__)
            input("\nEnter to leave")
    addInitScriptButton.click()

    # 更改語言
    sb.click('//span[contains(text(), "Jenny - Professional")]')
    # 選擇Chinese語言Filter
    time.sleep(1)
    sb.click('//div[contains(text(), "English")]')
    sb.click('//li[contains(text(), "Chinese")]')
    # 選擇HsiaoChen - Friendly聲音
    sb.click('//div[contains(text(), "HsiaoChen - Friendly")]')
    

    # 刪除Default文本（僅第一次）
    scriptInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]')))
    scriptInput.clear()

    #循環工作
    iter = 2
    lineFlag = 1
    pFlag = 1
    for paragraph in paragraphs:
        try:
            lines = paragraph.split('\n')
            for line in lines:
                scriptInput.send_keys(line.strip())
                if(lineFlag == len(lines)):
                    lineFlag = 1
                else:
                    scriptInput.send_keys(Keys.SHIFT,Keys.ENTER)
                    lineFlag +=1

            #get new button
            addScriptButtonXPath = f"/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[{iter}]/div[2]/button[1]"
            addScriptButton = wait.until(EC.presence_of_element_located((By.XPATH,addScriptButtonXPath )))


            if(pFlag == len(paragraphs)):
                pass
            else:
                try:
                    addScriptButton.click()
                except:
                    time.sleep(0.5)
                    addScriptButton.click()
                #get new scriptInput
                scirptInputButtonXPath = f"/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[{iter}]/div[2]/div[1]/div/div[2]/div/div[1]"
                scriptInput = wait.until(EC.presence_of_element_located((By.XPATH, scirptInputButtonXPath)))
            iter += 1
            pFlag += 1
        except Exception:
            print(Exception)
            print(Exception.args)
            print(Exception.__cause__)
            print(Exception.__context__)
            input()

    #完成後關閉瀏覽器
    input("請等待Heygen存檔完成，按下Enter關閉瀏覽器")