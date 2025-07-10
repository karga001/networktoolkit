import subprocess

def wireshark_run():
    subprocess.run('sudo wireshark', shell=True)