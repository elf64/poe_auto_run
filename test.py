import psutil
import time
import threading
from subprocess import Popen
import os

not_run = True

def is_process_running(name):
    """
        This function will return True or False if the process is running.
    :param name:
    :return:
    """
    for p in psutil.process_iter():
        if name in p.name():
            return True
    return False


def start():
    global not_run
    trade = None
    macro = None
    while 1:
        if is_process_running("PathOfExile_x64Steam.exe"):
            if not_run:
                trade = start_trade()
                macro = start_macro()
                not_run = False
            else: pass
        else:
            if not not_run:
                #Popen("TASKKILL /F /PID {pid} /T"
                #      .format(pid=trade.pid))
                #trade.kill()
                #macro.kill()
                #Popen("TASKKILL /F /PID {pid} /T"
                #      .format(pid=macro.pid))
                os.system("taskkill /f /im  AutoHotkey.exe")
                not_run = True
            else: pass
        time.sleep(5)


def start_trade():
    trade = Popen(
        ["C:\Program Files\AutoHotkey\AutoHotKey.exe",
         "D:\poeTrade\Run_TradeMacro.ahk"],
        shell=False
    )
    return trade

def start_macro():
    macro = Popen(
        ["C:\Program Files\AutoHotkey\AutoHotKey.exe",
         "D:\poeScripts\macro.ahk"],
        shell=False
    )
    return macro

x = threading.Thread(target=start)
x.start()
