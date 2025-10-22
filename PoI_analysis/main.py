import os
from os import walk

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

import tkinter as tk
from tkinter.filedialog import askopenfilename

import helper_func as helper
import algorithm_func as alg

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
    # print("main()")

    # filepath = read_file()

    # course = helper.open_file(filepath)

    while True:
        print("The following actions are available: ")
        print("Options: Select file (f), Quit (q)")
        choice = input('Input:  ')
        match choice:
            case "f":
                filepath = read_file()
                course = helper.open_file(filepath)
                while True:
                    print("The following actions are available: ")
                    print("Options: New File (f), Quit (q)")
                    print("Options: PoI 1.1 (11), PoI 1.2 (12)")
                    print("Options: PoI 2.1 (21), PoI 2.2 (22), PoI 2.3 (23), PoI 2.4 (24), PoI 2.5 (25)")
                    choice = input('Input:  ')
                    match choice:
                        case "f":
                            break
                        case "11":
                            alg.poi_11(course)
                        case "12":
                            alg.poi_12(course)
                        case "21":
                            alg.poi_21(course)
                        case "22":
                            alg.poi_22(course)
                        case "23":
                            alg.poi_23(course)
                        case "24":
                            alg.poi_24(course)
                        case "25":
                            alg.poi_25(course)
                        case "q":
                            print("Program exit.")
                            raise SystemExit
                        case _:
                            print("Did not catch that. Try again?")
            case "q":
                print("Program exit.")
                raise SystemExit
            case _:
                print("Did not catch that. Try again?")

main()