import tkinter
import requests

def say():
    url = "http://118.24.77.117:9501/admin/Login/test"
    result = requests.get(url,params={"a":"b"})
    print(result.text)

win = tkinter.Tk()
win.title("mysql")
win.geometry("400x500+300+200")

button = tkinter.Button(win,text="Button",command=say)
button.pack()

button1= tkinter.Button(win,text="关闭",command=win.quit,width=2,height=5)
button1.pack()


win.mainloop()