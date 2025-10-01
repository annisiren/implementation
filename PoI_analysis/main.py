import os
from os import walk
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

import tkinter as tk
from tkinter.filedialog import askopenfilename

import helper_func as helper


def read_file():
    print("Please give a file: ")
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    if os.path.exists(filepath):
        return filepath
    else:
        print("No file selected.")
    raise SystemExit


def main():
    print("main()")

    filepath = read_file()

    course = helper.open_file(filepath)


    helper.save_course(course)




main()