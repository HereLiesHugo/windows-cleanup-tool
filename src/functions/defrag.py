import subprocess

def defragDrive():
    subprocess.run("defrag c: /u /v")