import tkinter

win = tkinter.Tk()

win.title("mysql")
win.geometry("500x550+200+200")

label = tkinter.Label(win,
                      text="I am a good man",
                      bg="black",
                      fg="yellow",
                      font=("黑体",20)
                      ,width=100,
                      height=10
                      ,
                      wraplength=40,
                      justify='left',
                      anchor='w'
                      )
label.pack()

win.mainloop()