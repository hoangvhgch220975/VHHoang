from tkinter import messagebox as msg
from tkinter import *
question = [['What is the capital of France?', 'Paris', 'London', 'Berlin', 'Madrid', 1],
            ['What is the capital of Germany?', 'Paris', 'London', 'Berlin', 'Madrid',3],
            ['What is the capital of Spain?', 'Paris', 'London', 'Berlin', 'Madrid',4],
            ['What is the capital of England?', 'Paris', 'London', 'Berlin', 'Madrid',2]]
curr_question = 0        
### Event handlers 
def load_question(question_index):
    lbl_quiz['text'] = question[question_index][0]
    rd_option1['text'] = question[question_index][1]
    rd_option2['text'] = question[question_index][2]
    rd_option3['text'] = question[question_index][3]
    rd_option4['text'] = question[question_index][4]

def btn_answer_click():
    global curr_question
    if curr_question > 3:
        msg.showinfo('Info','End')
    else:
        if answer_choice.get() == question[curr_question][5]:
            msg.showinfo('Quiz','Correct answer')
        else:
            msg.showinfo('Quiz','Wrong answer')
    curr_question += 1
    load_question(curr_question)

def btn_next_click():
    global curr_question
    if curr_question > 3:
        msg.showinfo('Info','End')
        exit()
    else:
        curr_question += 1
        load_question(curr_question)
### Create window and widget

window = Tk()
window.title('Demo Radio ')
window.geometry('300x200')

lbl_quiz = Label(window, text = ' WHat is the capital of France?')
lbl_quiz.grid(row = 0, column= 0, columnspan=2)

answer_choice = IntVar()
rd_option1 = Radiobutton(window, text = 'Paris', value=1, var = answer_choice)
rd_option1.grid(row = 1, column=1, sticky=W)

rd_option2 = Radiobutton(window, text = 'London', value=2, var = answer_choice)
rd_option2.grid(row = 2, column=1, sticky=W)

rd_option3 = Radiobutton(window, text = 'Berlin', value=3, var = answer_choice)
rd_option3.grid(row = 3, column=1, sticky=W)

rd_option4 = Radiobutton(window, text = 'Madrid', value=4, var = answer_choice)
rd_option4.grid(row = 4, column=1, sticky=W)


btn_answer = Button(window, text = 'Answer', command = btn_answer_click)
btn_answer.grid(row = 5, column=0, sticky=W)

btn_next = Button(window, text ='Next', command = btn_next_click)
btn_next.grid(row =5, column=1, sticky=W)
window.mainloop()