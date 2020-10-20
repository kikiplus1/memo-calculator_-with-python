#!/usr/bin/env python
# coding: utf-8

# In[33]:


from tkinter import *
window = Tk()
window.title("진법계산기")



def twice():
    global an
    an = StringVar()
    
    a2 = Label(window, text="2진수를 입력해 주세요").grid(row= 6, column = 0)
    c1 = Entry(window, textvariable=an)
    c2 = Button(window, text= "변환하기", command=ch1)
    c1.grid(row= 7, column = 0)
    c2.grid(row= 8, column = 0)

def ch1():
 
    an1 = an.get()
    base = 2
    answer = int(an1,base)
    blank = Label(window, text= "" ).grid(row = 9,column=0 )
    an2 = Label(window, text= "결과 :").grid(row = 10,column=0 )
    an3 = Label(window, text=answer).grid(row= 11)
    
def ten():
    global te
    te= StringVar()
    
    an = StringVar()
    a3 = Label(window, text="10진수를 입력해 주세요").grid(row= 6, column = 0)
    d1 = Entry(window, textvariable=te)
    d2 = Button(window, text="변환하기", command=ch2 )
    d1.grid(row= 7, column = 0)
    d2.grid(row= 8, column = 0)
    
    
def ch2():
    te1 = te.get()
    re = bin(int(te1))
    re2 = str(re)
    blank2 = Label(window, text= "" ).grid(row = 9,column=0 )
    an2 = Label(window, text= "결과 :").grid(row = 10,column=0 )
    an3 = Label(window, text=re2[2:]).grid(row= 11)
    
  
a1 = Label(window, text ="버튼을 눌러주세요").grid(row=0)
b1 = Button(window, text = "2진법->10진법",command=twice)
b2 = Button(window, text = "10진법->2진법",command=ten)
b1.grid(row=1)
b2.grid(row=2)
window.mainloop()



# In[ ]:





# In[ ]:





# In[ ]:




