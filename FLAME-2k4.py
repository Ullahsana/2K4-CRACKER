import os, sys
try:
    __import__("poo").Main()
except Exception as e:
    exit(str(e))