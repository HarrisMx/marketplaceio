from datetime import datetime
from datetime import date
import os
import time

class Logs (object):
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
            _filename = os.path.join(os.getcwd(), "Logs", _filename)
            file = open(_filename, "a+")
            file.write(f"{current_time} - {msg}")
            file.write("\n")
            file.close()
        except Exception as exc:
            print(f"LogsHandler.py->recordLogs: Exception caught {str(exc)}")
            