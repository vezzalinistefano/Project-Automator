import subprocess
import sys

sp = subprocess

def creator (args):
    # create the project folder and navigate into it
    # than create the README.md file
    sp.call(["mkdir", args[1]])
    sp.call(["touch", args[1] + "/README.md"])
    sp.call(["git", "init", args[1] + "/"])



if __name__ == "__main__":
    creator(sys.argv)