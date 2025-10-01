import os
import func_helper as helper
import tkinter as tk
from tkinter.filedialog import askopenfilename


# Datastructure
# {ID1: { data for ID1 from CSV }, ID2: { data for ID2 from CSV } ... IDN: { data for IDN from CSV }}
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



# def main():
if __name__ == '__main__':
    filepath = read_file()
    file_df = helper.open_file(filepath)

    while True:
        print("The following actions are available: ")
        print("Options: Print current (p), Print graph (g), Quit (q)")
        choice = input('Input:  ')
        match choice:
            case "p":
                print(file_df.to_markdown())
            case "g":
                helper.build_graph(file_df)
            case "q":
                print("Program exit.")
                raise SystemExit
            case _:
                print("Did not catch that. Try again?")

