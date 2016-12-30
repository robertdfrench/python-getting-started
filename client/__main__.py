#!/bin/env python
import requests
import sys
import subprocess
import shlex
import os
import uuid


response = requests.get("https://olcf-ci-service.herokuapp.com/github-push-events/pop").json()
if 'data' not in response:
    print("No push events available right now")
    sys.exit(0)

push_event = response['data']
clone_url = push_event['repository']['clone_url']
commit = push_event['head_commit']['id']

def shell(command):
    print("$ %s" % command)
    subprocess.call(shlex.split(command))

repo_dir = "olcf-ci-%s" % uuid.uuid4()
shell("git clone %s %s" % (clone_url, repo_dir))
os.chdir(repo_dir)
shell("git checkout %s" % commit)
shell("./test.exe")
