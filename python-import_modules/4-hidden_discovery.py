#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() moduldakı bütün adları siyahı kimi qaytarır
    names = dir(hidden_4)
    
    # Adları əlifba sırası ilə düzürük və __ ilə başlayanları çıxdaş edirik
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
