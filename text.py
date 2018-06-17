

import tkinter

win = tkinter.Tk()

win.title("jakccsm")
win.geometry("400x300+200+200")

scroll = tkinter.Scrollbar()
text = tkinter.Text(win,width=200,height=2)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words""helli,every body,tongith i can tell u how to spell your standard english words""helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"
"helli,every body,tongith i can tell u how to spell your standard english words"


'''
text.insert(tkinter.INSERT,str)

win.mainloop()