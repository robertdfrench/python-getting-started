import subprocess
import shlex


def shell(command):
    print("$ %s" % command)
    subprocess.call(shlex.split(command))
