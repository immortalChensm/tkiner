import tkinter
#数值范围方法
win = tkinter.Tk()
win.title("jackcsm")
win.geometry("400x400+100+200")

spv = tkinter.StringVar()
#sp = tkinter.Spinbox(win,from_=0,to=100,increment=5,values=(0,2,4,6,8,10))
sp = tkinter.Spinbox(win,from_=0,to=100,increment=2,textvariable=spv)

sp.pack()

spv.set(50)
print(spv.get())


win.mainloop()