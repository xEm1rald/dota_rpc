from app import run
import sys
import os
import logging

if not sys.stdout:
    sys.stdout = open(os.devnull, "w")
if not sys.stderr:
    sys.stderr = open(os.devnull, "w")

if __name__ == '__main__':
    run()