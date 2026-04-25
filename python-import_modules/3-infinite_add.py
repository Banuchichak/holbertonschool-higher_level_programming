#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # sys.argv[0] skriptin adıdır, onu keçirik (index 1-dən başlayırıq)
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{}".format(total))
