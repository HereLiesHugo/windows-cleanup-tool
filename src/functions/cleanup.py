import subprocess
import os

def cleanup():
    print("Cleaning Files...")
    subprocess.run("cleanmgr /sagerun")
    os.system("pause")