import tkinter

win = tkinter.Tk()
win.title("jakccsm")
win.geometry("400x400+300+300")

lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
for item in ['china','japanese','korea','uk']:
    lb.insert(tkinter.END,item)

lb.pack()

win.mainloop()