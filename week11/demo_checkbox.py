from tkinter import *
from tkinter import messagebox as msg
#### EVENT HANDLER #####
def btn_calculate_click():
    n_nights = int(txt_nights.get())
    total = n_nights * 100
    if breakfast_check.get():
        total += n_nights *5
    if late_check.get():
        total +=20
    lbl_payment['text'] = f'Payment ${total}'
    


#### CREATE WINDOW #####
window = Tk()
window.title("Check box")
window.geometry("300x200")

#### CREATE WIDGET ####
lbl_title = Label(window, text = 'Room Booking Service')
lbl_title.grid(row = 0, column= 0, columnspan=3)

lbl_nights = Label(window, text ='Nights: ')
lbl_nights.grid(row = 1,column = 0, columnspan=2, sticky=W)

txt_nights = Entry(window, width=10)
txt_nights.grid(row = 1, column=1)

lbl_extras = Label(window, text ='Extras: ')
lbl_extras.grid(row = 2, column = 0)

breakfast_check = BooleanVar()
chk_breakfast = Checkbutton(window, text ='Breakfast (5$): ',var = breakfast_check, command= btn_calculate_click)
chk_breakfast.grid(row = 2, column =1, columnspan=2, sticky=W)

late_check = BooleanVar()
chk_late_checkout = Checkbutton(window, text ='Late checkout (20$): ', var = late_check, command= btn_calculate_click)
chk_late_checkout.grid(row = 3, column = 1, columnspan=2, sticky=W)

lbl_payment = Label(window, text ='Payment: ')
lbl_payment.grid(row = 4, column =0 , columnspan=2, sticky=W)


lbl_calculate = Button(window, text ='Calculate', command = btn_calculate_click)
lbl_calculate.grid(row = 4, column=2)

### START THE GUI ###
window.mainloop()