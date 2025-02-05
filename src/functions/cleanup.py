import subprocess

def cleanup():
    print("Cleaning Files...")
    subprocess.run("cleanmgr /sagerun")