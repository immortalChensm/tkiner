import tkinter

win = tkinter.Tk()
win.title("jackcms")
win.geometry("400x400+200+200")

def update():
    print(rb.get())
#rb = tkinter.IntVar()
rb = tkinter.StringVar()

radiobutton = tkinter.Radiobutton(win,text='男',value='male',variable=rb,command=update)
radiobutton.pack()
radiobutton1 = tkinter.Radiobutton(win,text='女',value='female',variable=rb,command=update)
radiobutton1.pack()

win.mainloop()