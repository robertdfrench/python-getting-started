import shlex
import os
import uuid


def run(push_event):
    repo_dir = "olcf-ci-%s" % uuid.uuid4()
    shell("git clone %s %s" % (push_event.clone_url, repo_dir))
    os.chdir(repo_dir)
    shell("git checkout %s" % push_event.commit)
    shell("./test.exe")
