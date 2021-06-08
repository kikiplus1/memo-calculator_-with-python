

from tkinter import *     # 파이썬에서 GUI 구현 가능한 모듈을 불러온다.
window = Tk()                    #윈도우창 실행 (gui)
window.title("간단사칙계산기")      #gui창 제목 설정

global first, second
first, second = "",""


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
    

global value
value=StringVar()
value.set(str(second))



wind = Entry(window, textvariable= value,  justify='right' ).grid(columnspan=5)


clear = Button(window, text = "CLEAR",command=clear, width=5, height =2).grid(row=1, column =0)
dele = Button(window, text = "",command=pu3, width=5, height =2).grid(row=1, column =1)
tot = Button(window, text = "=", width=5, height =2, command=result).grid(row=1, column =2)
plus = Button(window, text = "+",command=plus1, width=5, height =2).grid(row=1, column =3)

num1 = Button(window, text = "1",command=pu1, width=5, height =2).grid(row=2, column =0)
num2 = Button(window, text = "2",command=pu2, width=5, height =2).grid(row=2, column =1)
num3 = Button(window, text = "3",command=pu3, width=5, height =2).grid(row=2, column =2)
minu = Button(window, text = "-",command=min1, width=5, height =2).grid(row=2, column =3)

num4 = Button(window, text = "4",command=pu4, width=5, height =2).grid(row=3, column =0)
num5 = Button(window, text = "5",command=pu5, width=5, height =2).grid(row=3, column =1)
num6 = Button(window, text = "6",command=pu6, width=5, height =2).grid(row=3, column =2)
mu = Button(window, text = "x",command=mu1, width=5, height =2).grid(row=3,column =3)

num7 = Button(window, text = "7",command=pu7, width=5, height =2).grid(row=4, column =0)
num8 = Button(window, text = "8",command=pu8, width=5, height =2).grid(row=4, column =1)
num9 = Button(window, text = "9",command=pu9, width=5, height =2).grid(row=4, column =2)
divi = Button(window, text = "/",command=divi1, width=5, height =2).grid(row=4, column =3)


num0 = Button(window, text = "0", width=5, height =2,command=pu0).grid(row=5, column =0)
le = Button(window, text = "(", width=5, height =2,command=le).grid(row=5, column =1)
ri = Button(window, text = ")", width=5, height =2,command=ri).grid(row=5, column =2)
blank3 = Button(window, text = "", width=5, height =2).grid(row=5, column =3)


blank = Button(window, text = "2진법", width=5, height =2, command = twi).grid(row=6, column =0)
blank1 = Button(window, text = "8진법", width=5, height =2, command = oc).grid(row=6, column =1)
blank2 = Button(window, text = "16진법", width=5, height =2, command=hx).grid(row=6, column =2)
blank4 = Button(window, text = "", width=5, height =2).grid(row=6, column =3)

window.mainloop()




