from tkinter import *
from tkinter import messagebox as msg
#### EVENT HANDLER #####
def btn_add_click():
    a = int(txt_a.get()) #get content of entry txt_a
    b = int(txt_b.get()) #get content of entry txt_b
    result = a + b
    lbl_results.config(text = result) #set text of label lbl_results
  
def btn_sub_click():
    a = int(txt_a.get()) 
    b = int(txt_b.get())
    result = a - b
    lbl_results.config(text = result) 

def btn_multi_click():
    a = int(txt_a.get()) 
    b = int(txt_b.get())
    result = a * b
    lbl_results.config(text = result)

def btn_divide_click():
    a = int(txt_a.get()) 
    b = int(txt_b.get())
    result = a / b
    lbl_results.config(text = result)

def operator(op):
    a = int(txt_a.get()) 
    b = int(txt_b.get())
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    lbl_results.config(text = result)

#### CREATE WINDOW #####
window = Tk()
window.title("Arithmetic Operations")
window.geometry("300x200")
#### CREATE WIDGET #####
lbl_a = Label(window, text="a = ")
lbl_a.grid(row= 0, column= 0 )

txt_a = Entry(window, width=10)
txt_a.grid(row= 0, column=1)

lbl_b = Label(window, text="b = ")
lbl_b.grid(row= 1, column=0 )

txt_b = Entry(window, width=10)
txt_b.grid(row = 1, column=1)

lbl_c = Label(window, text="Result =")
lbl_c.grid(row = 2, column =0)

lbl_results = Label(window, text='')
lbl_results.grid(row = 2, column =1, sticky=W)

btn_add = Button(window, text="Add", width=8, command = btn_add_click)
btn_add.grid(row = 4, column =1, sticky=W)

btn_sub = Button(window, text="Sub", width=8, command = btn_sub_click)
btn_sub.grid(row = 4, column =2, sticky=W)

btn_multi = Button(window, text="Mul", width=8, command = btn_multi_click)
btn_multi.grid(row = 5, column =1, sticky=W)

btn_divide = Button(window, text="Divide", width=8, command = btn_divide_click)
btn_divide.grid(row = 5, column =2, sticky=W)


window.mainloop()