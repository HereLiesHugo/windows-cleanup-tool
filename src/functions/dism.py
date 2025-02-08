import subprocess, os

def dismScan():
    print("Checking For Corruption")
    subprocess.run("DISM.exe /Online /Cleanup-Image /ScanHealth")
    print("Checking if Corruption is Repairable")
    subprocess.run("DISM.exe /Online /Cleanup-Image /CheckHealth")
    print("Repairing if Possible")
    subprocess.run("DISM.exe /Online /Cleanup-Image /RestoreHealth")
    
    os.system("pause")