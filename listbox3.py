import tkinter

win = tkinter.Tk()
win.title("jackcsm")
win.geometry("400x400+200+200")
#selectmode=tkinger.SINGLE tkinkger.BROSWER think.EXTENDED
listbox = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
itemArr = 'china is a developing country that has huge market'
for item in itemArr:
    listbox.insert(tkinter.ACTIVE,item)


scrollbar = tkinter.Scrollbar()
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox.configure(yscrollcommand=scrollbar.set)

listbox.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
scrollbar['command'] = listbox.yview

win.mainloop()