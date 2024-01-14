from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from book import load_books,load_names

books = load_books()
names = load_names(books)
### EVENT HANDLER
def lst_book_selected(event):
    #get book name from list of books
    book = lst_book.get(lst_book.curselection())
    #set book info from dictionary
    txt_name.delete(0, END) #clear current text
    txt_name.insert(0, book) #insert new text(name of book)
    txt_author.delete(0, END) 
    txt_author.insert(0, books[book][0])
    txt_price.delete(0, END)
    txt_price.insert(0, books[book][1]) 

def ok_click():
    total = 0
    price = float(txt_price.get())
    quantity = int(txt_quantity.get())
    deliver_index = cbb_delivery.current()
    total = price * quantity
    if deliver_index == 0: #standard delivery
        total +=1
    elif deliver_index ==1: #fast delivery
        total +=3
    else: 
        total +=5 #express delivery
    # add cover fee if selected
    if cover_choice.get() == True:
        total +=2
    msg.showinfo("Total", f'Total: {total}$')

def cancel_click():
    #clear all text
    txt_name.delete(0, END) #clear current text
    txt_author.delete(0, END)   
    txt_price.delete(0, END)
    txt_quantity.delete(0, END)
    cbb_delivery.delete(0,END)

### CREATE WINDow
window = Tk()
window.title('Book store ')
window.geometry('500x400')

### CREATE WIDGET
lbl_book = Label(window, text = 'Book')
lbl_book.grid(row=0, column=0, sticky=W)

lst_book = Listbox(window, height=5, selectmode = SINGLE)
lst_book.grid(row=1, column=0, columnspan=2, rowspan=3, sticky=W, padx=20)
for name in names:
    lst_book.insert(END, name)
lst_book.bind('<<ListboxSelect>>',lst_book_selected)
lbl_name = Label(window, text = 'Name: ')
lbl_name.grid(row=1, column= 3, sticky=W)

txt_name = Entry(window, width=10)
txt_name.grid(row=1, column=4, columnspan=2, sticky=W)

lbl_author = Label(window, text = 'Author: ')
lbl_author.grid(row=2, column=3, sticky=W)

txt_author = Entry(window, width=10)
txt_author.grid(row=2, column=4, columnspan=2, sticky=W)

lbl_price = Label(window, text = 'Price: ')
lbl_price.grid(row=3, column=3, sticky=W)

txt_price = Entry(window, width=10)
txt_price.grid(row=3, column=4, columnspan=2, sticky=W)

lbl_Quantity = Label(window, text='Quantity: ')
lbl_Quantity.grid(row = 4, column=0, sticky=W)

txt_quantity = Entry(window, width=10)
txt_quantity.grid(row=4, column=1, sticky=W)

lbl_delivery = Label(window, text='Delivery: ')
lbl_delivery.grid(row=5, column=0, sticky=W)

cbb_delivery = Combobox(window, width=10)
cbb_delivery["values"] = ('Standard (1$)', 'Fast (3$)', 'Express (5$)')
cbb_delivery.grid(row=5, column=1, sticky=W)

lbl_cover = Label(window, text='Cover (2$): ')
lbl_cover.grid(row=5, column=2, sticky=W)

cover_choice = IntVar()
rd_cover_yes = Radiobutton(window, text='Yes', value=1, var = cover_choice)
rd_cover_yes.grid(row=5, column=3, sticky=W)

rd_cover_no = Radiobutton(window, text='No', value=2, var = cover_choice)
rd_cover_no.grid(row=5, column=4, sticky=W)

ok = Button(window, text='OK', width=5, command= ok_click)
ok.grid(row=6, column=3, sticky=W)

cancel = Button(window, text='Cancel', width=5, command=cancel_click)
cancel.grid(row=6, column=4, sticky=W)
window.mainloop()