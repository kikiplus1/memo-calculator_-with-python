#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import *
from tkinter.filedialog import *

name = "제목없음"
global first, second
first, second = "",""

def newfile():
    global name
    name = "제목없음"
    text.delete(0.0, END)
    
def savefile():
    global name
    t = text.get(0.0,END)
    f = open(filename,'w')
    f.write(t)
    f.close()
    
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="오류", message="저장되지 않았습니다..")

def openfile():
    global name
    f= askopenfile(mode='r')
    name = f.name
    t= f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

def insertt():
    text.insert(END,str(show))
    text.insert(END,str(tw)[2:])
def pu1():
    global second
    second += "1"
    value.set(str(second))

    
def pu2():
    global second
    second += "2"
    value.set(str(second))
    
def pu3():
    global second
    second += "3"
    value.set(str(second))

    
def pu4():
    global second
    second += "4"
    value.set(str(second))
    
def pu5():
    global second
    second +="5" 
    value.set(str(second))
    
    
def pu6():
    global second
    second += "6"
    value.set(str(second))
    
def pu7():
    global second
    second += "7"
    value.set(str(second))
    
    
def pu8():
    global second
    second += "8"
    value.set(str(second))
    
    
def pu9():
    global second
    second += "9"
    value.set(str(second))

    
def pu0():
    global second
    second += "0"
    value.set(str(second))
    
    
def plus1():
    global second, op
    second += "+"
    value.set(str(second))
    
    
def min1():
    global first, second, op
    second += "-"
    value.set(str(second))
    
    
    
def divi1():
    global first, second, op
    second += "/"
    value.set(str(second))

    
def mu1():
    global first, second, op
    second += "*"
    value.set(str(second))
    
def le():
    global first, second, op
    second += "("
    value.set(str(second))
    
def ri():
    global first, second, op
    second += ")"
    value.set(str(second))
    
def result():
    global first, second, op, show
    
    show = eval(second)
    second = str(show)
    value.set(str(show))
        
def clear():
    global first, second, show, op ,tw
    second = ""
    show = ""
    tw=0
    value.set(str(second))
  
              
def twi():
    global second, tw 
    tw = bin(int(second))
    value.set(str(tw)[2:])
              

def oc():
    global second, tw
    tw = oct(int(second))
    value.set(str(tw)[2:])

def hx():
    global second, tw 
    tw = hex(int(second))
    value.set(str(tw)[2:])
    

window = Tk()
window.title("소프트웨어학과 20181719 정희선")
window.geometry("905x278")
window.resizable(False, False)


frame1=Frame(window, width=300, height=400)
frame1.pack(side = 'left')

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config()



text= Text(frame1, width=100, height=400, yscrollcommand=scrollbar.set )
text.pack()


menubar = Menu(window)
m = Menu(menubar,tearoff=0)
m.add_command(label="저장", command = savefile)
m.add_command(label="다른이름으로 저장", command=saveAs)
menubar.add_cascade(label="저장",menu=m)

m1 = Menu(menubar,tearoff=0)
m1.add_command(label="새로만들기", command = newfile)
m1.add_command(label="열기", command = openfile)
menubar.add_cascade(label="열기",menu=m1)
window.config(menu=menubar)



global value
value=StringVar()
value.set(str(second))




frame2=Frame(window)


wind = Entry(frame2, textvariable= value, justify='right' ).grid(columnspan=5)

clear = Button(frame2, text = "CLEAR",command=clear, width=5, height =2).grid(row=1, column =0)
dele = Button(frame2, text = "",command=pu3, width=5, height =2).grid(row=1, column =1)
tot = Button(frame2, text = "=", width=5, height =2, command=result).grid(row=1, column =2)
plus = Button(frame2, text = "+",command=plus1, width=5, height =2).grid(row=1, column =3)

num1 = Button(frame2, text = "1",command=pu1, width=5, height =2).grid(row=2, column =0)
num2 = Button(frame2, text = "2",command=pu2, width=5, height =2).grid(row=2, column =1)
num3 = Button(frame2, text = "3",command=pu3, width=5, height =2).grid(row=2, column =2)
minu = Button(frame2, text = "-",command=min1, width=5, height =2).grid(row=2, column =3)

num4 = Button(frame2, text = "4",command=pu4, width=5, height =2).grid(row=3, column =0)
num5 = Button(frame2, text = "5",command=pu5, width=5, height =2).grid(row=3, column =1)
num6 = Button(frame2, text = "6",command=pu6, width=5, height =2).grid(row=3, column =2)
mu = Button(frame2, text = "x",command=mu1, width=5, height =2).grid(row=3,column =3)

num7 = Button(frame2, text = "7",command=pu7, width=5, height =2).grid(row=4, column =0)
num8 = Button(frame2, text = "8",command=pu8, width=5, height =2).grid(row=4, column =1)
num9 = Button(frame2, text = "9",command=pu9, width=5, height =2).grid(row=4, column =2)
divi = Button(frame2, text = "/",command=divi1, width=5, height =2).grid(row=4, column =3)


num0 = Button(frame2, text = "0", width=5, height =2,command=pu0).grid(row=5, column =0)
le = Button(frame2, text = "(", width=5, height =2,command=le).grid(row=5, column =1)
ri = Button(frame2, text = ")", width=5, height =2,command=ri).grid(row=5, column =2)
blank3 = Button(frame2, text = "", width=5, height =2).grid(row=5, column =3)


blank = Button(frame2, text = "2진법", width=5, height =2, command = twi).grid(row=6, column =0)
blank1 = Button(frame2, text = "8진법", width=5, height =2, command = oc).grid(row=6, column =1)
blank2 = Button(frame2, text = "16진법", width=5, height =2, command=hx).grid(row=6, column =2)
insertt = Button(frame2, text = "쓰기", width=5, height =2, command=insertt).grid(row=6, column =3)
frame2.pack(side = 'left')



window.mainloop()


    


# In[ ]:




