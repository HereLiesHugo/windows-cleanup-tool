import os
from pathlib import Path


pycwd = str(os.getcwd())
usrDir = Path.home()
chromeCBat = pycwd + r"\bat\chrome_cache_del.bat"
firefoxCBat = pycwd + r"\bat\firefox_cache_del.bat"
msedgeCBat = pycwd + r"\bat\msedge_cache_del.bat"

def brCleanUp():
    print("Select Browser (enter number): \n")
    print("1. Chrome\n")
    print("2. Firefox\n")
    print("3. Edge (New/2020)\n")

    opt = input()

    if opt == '1':
        os.startfile(chromeCBat)
        print("Deleting Chrome Cache")
    elif opt == '2':
        os.startfile(firefoxCBat)
        print("Deleting Firefox Cache")
    elif opt == '3':
        os.startfile(msedgeCBat)
        print("Deleting MSEdge Cache")

    os.system("pause")