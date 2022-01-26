import time
import sys
import os
import pyperclip
from pytz import timezone
from datetime import datetime
import time

if __name__ == "__main__":
    sys.path.append(os.path.abspath("SO_site-packages"))

    file_name = "clipboard_log.txt"
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste().replace('\r\n','\n') # windows용으로 개행문자 수정
        if tmp_value != recent_value:
            with open(file_name, "a", encoding='utf-8') as f:
                f.write(datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M')+"\n")
                f.write(tmp_value)
                f.write("\n\n")
            recent_value = tmp_value
            print(f"{datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M')} Value changed: {str(recent_value)}")
        time.sleep(1)