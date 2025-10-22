import os
from os import walk
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

import matplotlib.pyplot as plt
import pandas as pd

import tkinter as tk
from tkinter.filedialog import askopenfilename

import sop_obj as func
import func_helper as helper


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
    complete_header_list = ['tier','title','LS: Perception','LS: Input','LS: Organization','LS: Processing','LS: Understanding','CT','D','BT','P']

    filepath = read_file()

    course = helper.open_file(filepath)

    # c_tree = helper.tree(course)
    # paths = helper.get_paths(c_tree)
    # print(paths)
    # helper.lp_creator(paths)

    # print(paths)

    # helper.save_course(course)




main()