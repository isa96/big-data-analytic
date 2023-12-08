#!/usr/bin/python
"""mapper.py"""
import sys
import re

for line in sys.stdin:
    line = re.sub(r'[^\w\s]', '', line)
    line = line.strip()
    words=line.split()
    for word in words:
        print(f"{word.lower()}\t1")