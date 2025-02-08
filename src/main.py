import ctypes, sys, os
import functions.dism as dism
import functions.cleanup as clean
import functions.temp_cleanup as tcl
import functions.browser_cleanup as brcl
import functions.defrag as defrag
import functions.file_integ_check as fic

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

print("Welcome to windows cleanup!\n")

# Options
print("1. Run DISM (Corruption Cleanup)\n")
print("2. Run cleanmgr (File Cleanup)\n")
print("3. Clean Temp Files\n")
print("4. Clean Browser Temp Files\n")
print("5. Defragment C: Drive\n")
print("6. Verify File Integrity\n")

opt = input("Please select an option:\n")

if is_admin():
    # Options
    if opt == '1':
        dism.dismScan()
    elif opt == '2':
        clean.cleanup()
    elif opt == '3':
        tcl.tmpCln()
    elif opt == '4':
        brcl.brCleanUp()
    elif opt == '5':
        defrag.defragDrive()
    elif opt == '6':
        fic.fic()

else:
    # Re-run the program with admin rights
    print("You must be admin to run this script. Elevating UAC...\n")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)