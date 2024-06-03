from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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


# Init
driver = webdriver.Chrome()
driver.get("https://app.heygen.com/home")
action = ActionChains(driver)

#等待使用者手動登入
input("請手動登入Heygen並進入要匯入字幕的draft頁面，完成後按Enter繼續...")

# 等待並點擊add script
wait = WebDriverWait(driver, 10)
addInitScriptButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[4]/div[2]')))
addInitScriptButton.click()

# 更改語言
languageButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]')))
languageButton.click()

# 選擇Chinese語言Filter
time.sleep(0.5)
try:
    chineseOption = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div')))
except:
    chineseOption = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div')
chineseOption.click()
chineseOption = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/ul/li[5]')))
chineseOption.click()


# 選擇HsiaoChen - Friendly聲音
voiceOption = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]')))
voiceOption.click()

# 刪除Default文本（僅第一次）
scriptInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]')))
scriptInput.clear()

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
        print("Here\n\n\n")
        print(Exception)
        print(Exception.args)
        print(Exception.__cause__)
        print(Exception.__context__)
        input()

input("Click to leave")
#完成後關閉瀏覽器
#driver.quit()