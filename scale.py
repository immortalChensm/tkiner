import tkinter

win = tkinter.Tk()
win.title("scale")
win.geometry("400x400+200+250")
#水平滑块

scable = tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,tickinterval=10,length=200)

scable.set(20)

tkinter.Button(win,text='click',command=lambda :print(scable.get())).pack()
scable.pack()
win.mainloop()