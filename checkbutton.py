

import tkinter

win = tkinter.Tk()
win.title("jack")
win.geometry("400x400+200+200")

hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()
def update():
    message = ''
    if hobby1.get() == True:
        message+="money\n"
    if hobby2.get == True:
        message+="power\n"
    if hobby3.get() == True:
        message+="bfBeauty"

    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)

checkbutton1 = tkinter.Checkbutton(win,text='money',variable=hobby1,command=update)
checkbutton1.pack()
checkbutton2 = tkinter.Checkbutton(win,text='power',variable=hobby2,command=update)
checkbutton2.pack()
checkbutton3 = tkinter.Checkbutton(win,text='BaiFuBeauty',variable=hobby3,command=update)
checkbutton3.pack()

text = tkinter.Text(win,width=50,height=4)
text.pack()

win.mainloop()