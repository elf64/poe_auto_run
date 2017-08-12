import os
import psutil
import time
import threading

def start_scripts():
    """
        This function will start the scripts.
        Currently this is very buggy because if you have any other .ahk scripts running
            this function will not run!!!
    :return:
    """
    if is_process_running("AutoHotkey.exe"):
        return
    os.system("D:\poeTrade\Run_TradeMacro.ahk")
    os.system("D:\poeScripts\macro.ahk")

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

def kill_scripts(is_run):
    """
        This function will kill every .ahk script that is running.
    :return:
    """
    if is_run:
        os.system("taskkill /f /im  AutoHotkey.exe")
    else:
        pass
try:
    while 1:
        if is_process_running("PathOfExile_x64Steam.exe"):
            t3 = threading.Thread(target=start_scripts)
            t3.start()
        else:
            kill_scripts(is_process_running("AutoHotkey.exe"))
        time.sleep(1)
except Exception as e:
    with open("error_log_file", "a") as f:
        f.write(e)
        f.close()
