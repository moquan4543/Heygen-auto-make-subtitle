# Heygen-auto-make-subtitle  
* * *
2023/5/30更新  
不再自動更改語言  
不再自動調整語速  
使用前須確保第一頁「ADD SPEECH」按鈕已被點下，且語言已更改  
執行前一定要讓新增文字上方的Text Script「完整的」顯示在螢幕上  
* * *
Github上我放的是源碼，可以在這裡下載打包的exe，點兩下就可以執行  
https://drive.google.com/drive/folders/1ubwqH3clQhdqA_7Hi0keSKVYomL0gQe7?usp=share_link  
基本上只要下載rar檔解壓縮就行，另外兩個src跟exe檔只是避免壓縮損壞什麼的，跟壓縮檔裡是一樣的東西
* * *
參考流程:  
1.剪映輸出字幕選txt檔  
2.手動根據老師講的內容分好哪幾句話是同一頁PPT中講的，不同頁的內容用連續10至50個字母'a'來分隔  
3.將改好的txt檔放到與程式的同層資料夾  
4.回到Heygen，手動將進度條拉至第一張投影片，按add speech並更改語言  
5.確保Text Script的紫色icon有顯示在螢幕上  
6.執行程式，輸入路徑  
* * *
## **autosubtitle.py**  
利用Pyautogui在螢幕上尋找指定的位置，並模擬滑鼠及鍵盤操作  
因為增加字幕很機械化  
就是一直複製貼上然後換下一頁  
所以我就寫了一支程式幫我做  
有時候可能會失敗  
如果失敗只要在command line按Ctrl+C強制中斷  
然後讓Heygen回到原始的狀態  
再重新執行程式即可
## **convertSRT.py**  
可以利用此程式將srt檔轉換為純文字  
* * *
參考資料/工具:  
馴碼快手(一鍵繁簡轉換):https://www.azofreeware.com/2012/05/20050305.html  
* * *
code by 謝梓翔
