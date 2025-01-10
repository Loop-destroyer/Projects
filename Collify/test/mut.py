#!D:\Projects\venv\Scripts\python.exe

#!D:\Projects\venv\Scripts\python.exe

import sys
import importlib.util
from mutpy import commandline

# Replace find_loader with find_spec
def find_loader(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec.loader if spec else None

if __name__ == '__main__':
    commandline.main(sys.argv)