import os
from datetime import datetime, date
import time

class LogsHandler(object):
    __path = os.path.join(os.getcwd(), 'Logs')

    def __init__(self):
        pass
    
    @staticmethod
    def recordLogs(msg):
        try:
            today = date.today()
            _filename = today.strftime("%d-%m-%Y")
            _filename = f"{str(_filename)}.txt"

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            _filename = os.path.join(LogsHandler.__path,_filename)

            f = open(_filename, "a+")
            f.write(f"{current_time} - {msg}")
            f.write("\n")
            f.close()
        except Exception as exc:
            print(f"LogsHandler Exception: {str(exc)}")