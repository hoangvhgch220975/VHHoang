from tkinter import *
from tkinter import messagebox as msg
#### EVENT HANDLER #####
def btn_OK_Clicked():
    msg.showinfo('Info','OK button clicked')

#### CREATE WINDOW #####
window = Tk()
window.title("Hello GUI App")
window.geometry("300x200")

#### CREATE WIDGET #####
lbl_massage = Label(window, text= 'Hello World')
lbl_massage.grid(row =0, column =0)

lbl_pythons = Label(window, text = 'Hello Python')
lbl_pythons.grid(row =1, column=1)

btn_OK = Button(window, text = 'OK', command = btn_OK_Clicked)
btn_OK.grid(row =2, column=2)

### START THE GUI ###
window.mainloop()