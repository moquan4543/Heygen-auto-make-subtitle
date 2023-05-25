import os
import re
import os.path
# 設定讀取和輸出的目錄
src_dir = 'read/dir'
build_dir = 'output/dir'

# 讀取 src 目錄下的 .srt 檔案
for filename in os.listdir(src_dir):
    if filename.endswith('.srt'):
        with open(os.path.join(src_dir, filename), 'r', encoding='utf-8') as f:
            text = f.read()

        # 使用正則表達式批次尋找並取代
        text = re.sub(r'\s\n[0-9][0-9][0-9]', '', text)
        text = re.sub(r'\s\n[0-9][0-9]', '', text)
        text = re.sub(r'\s\n[0-9]', '', text)
        text = re.sub(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9] --> .*\n', '', text)
        text = re.sub(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9] --> .*\n', '', text)
        text = re.sub(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9] --> .*\n', '', text)

        # 刪除第一行
        text = text.split('\n', 1)[1]

        # 將結果寫入新檔案
        output_filename = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(build_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        # 將結果輸出到console
        with open(output_path, 'r', encoding='utf-8') as f:
            output_text = f.read()
            print(f'******** {output_filename} ********')
            print(output_text)
