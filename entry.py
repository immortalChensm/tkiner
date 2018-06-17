import tkinter

win = tkinter.Tk()
win.title("mysql")
win.geometry("400x500+500+100")

e = tkinter.Variable()

entry = tkinter.Entry(win,textvariable=e)

e.set("hello,world")

button = tkinter.Button(win,text="click",command=lambda :print(e.get()))
button.pack()
entry.pack()


win.mainloop()
