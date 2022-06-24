import subprocess


def pull():
    subprocess.run(["git", "pull"])