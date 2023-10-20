#!/usr/bin/env python
import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(word + "\t1")
