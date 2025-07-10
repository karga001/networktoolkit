import os
import subprocess

def burpsuite_run():
    kur = str(input("Burpsuite kurulu mu? E/H"))
    if kur == "e":
        subprocess.run('burpsuite', shell=True)
    else:
        print("önce burpsuite'i kur")