import subprocess
import sys
import os
from github import Github

sp = subprocess
g = Github("your access token")
# alternately
# g = Github("username","password")


def creator (args):
    # create the project folder and navigate into it
    # than create the README.md file
    sp.call(["mkdir", args[1]])
    sp.call(["touch", args[1] + "/README.md"])
    
    # git init and remote repository creation
    sp.call(["git", "init", args[1] + "/"])
    g.get_user().create_repo(args[2])

    #origin url creation
    originUrl = "https://github.com/" + g.get_user().login + "/" + args[2] + ".git"

    sp.call(["git", "remote", "add", "origin", originUrl], cwd=args[1] + "/")
    sp.call(["git", "add", "."], cwd=args[1] + "/")
    sp.call(["git", "commit", "-m", "Initial Commit"], cwd=args[1] + "/")
    sp.call(["git", "push", "origin", "master"], cwd=args[1] + "/")
    sp.call(["git", "push", "origin", "master"], cwd=args[1] + "/")

if __name__ == "__main__":
    creator(sys.argv)