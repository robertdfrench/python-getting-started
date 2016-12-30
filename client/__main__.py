#!/bin/env python
import time
from client.util import shell
from client import push_event
from client import run_ci

def try_ci():
    pe = push_event.next()
    if pe:
        run_ci.run(pe)
    else:
        print("No push events available right now")

while True:
    try_ci()
    time.sleep(10)
