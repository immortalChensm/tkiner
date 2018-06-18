import tkinter

win = tkinter.Tk()
win.title("jackcsm")
win.geometry("500x500+200+250")

lbv = tkinter.StringVar()

lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.insert(tkinter.END,'jack')
lb.insert(tkinter.ACTIVE,'tom')
for item in ['representative','democracy','grocery']:
    lb.insert(tkinter.END,item)

def update():
    #print(lbv.get())
    #print(lbv.get(lb.curselection()[0]))
    print(lb.get(lb.curselection()[0]))
button = tkinter.Button(win,text='click',width=50,height=2,command=update)
button.pack()
lb.pack()

#event bind
def myClick(e):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>",myClick)

win.mainloop()