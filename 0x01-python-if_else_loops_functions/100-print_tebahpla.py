#!/usr/bin/python3
idx = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - idx)), end="")
    idx = 32 if idx == 0 else 0
