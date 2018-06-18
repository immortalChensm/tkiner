
import tkinter

for item in dir(tkinter):
    print(type(item),help(tkinter[item]))