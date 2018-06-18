import tkinter

win = tkinter.Tk()
win.title("jackdsm")
win.geometry("500x500+200+300")

menubar = tkinter.Menu(win)
win.config(menu=menubar)

menu1 = tkinter.Menu(menubar,tearoff=False)

for item in ['PHP','PYTHON','JS','C','REDIS','SQL','exit']:
    if item == 'exit':

        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=lambda :print('jackcsm'))

menubar.add_cascade(label='language',menu=menu1)

menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label='red')
menu2.add_command(label='green')

menubar.add_cascade(label='color',menu=menu2)
win.mainloop()