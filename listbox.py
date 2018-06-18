import tkinter

win = tkinter.Tk()
win.title("jackcsm")
win.geometry("400x400+200+200")

lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()

for item in ['china','power','nuclear','weapon']:
    lb.insert(tkinter.END,item)
lb.insert(tkinter.ACTIVE,'country')
lb.insert(tkinter.END,['rich','spirit'])

#lb.delete(1)
#lb.delete(1,5)

#lb.select_set(1,3)
#lb.select_clear(1,2)
lb.select_set(1,5)
def getsize():
    #print(lb.size())
    #print(lb.get(2))
    #print(lb.get(2,5))
    #print(lb.curselection())
    print(lb.select_includes(1))
    print(lb.select_includes(6))
button = tkinter.Button(win,text='click',width=100,height=40,command=getsize)
button.pack()

win.mainloop()