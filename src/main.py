import ctypes, sys, os
import functions.dism as dism
import functions.cleanup as clean

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

print("Welcome to windows cleanup!\n")

# Options
print("1. Run DISM (Corruption Cleanup)\n")
print("2. Run cleanmgr (File Cleanup)\n")


opt = input("Please select an option:\n")

if is_admin():
    # Options
    if opt == '1':
        dism.dismScan()
    elif opt == '2':
        clean.cleanup()
else:
    # Re-run the program with admin rights
    print("You must be admin to run this script. Elevating UAC...\n")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)