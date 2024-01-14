from tkinter import *
from tkinter.ttk import Combobox

movies_list = ['The Matrix', 'The Lord of the Rings', 'The Dark Knight','Inception', 'Inerstellar']
movies_dict = {'The Matrix': ['Lana Wachowski, Lilly Wachowski', 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss'], \
                'The Lord of the Rings': ['Peter Jackson', 'Elijah Wood, Ian McKellen, Orlando Bloom'], \
                'The Dark Knight': ['Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart'], \
                'Inception': ['Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'], \
                'Interstellar': ['Christopher Nolan', 'Matthew McConaughey, Anne Hathaway, Jessica Chastain']}
### EVENT HANDLER
def cbb_movie_selected(event):
    # get movie's name
    movie = cbb_movie.get()
    #set movie info from the dictionary
    director = movies_dict[movie][0]
    actors = movies_dict[movie][1]
    lbl_director['text'] = f'Director: {director}'
    lbl_actors['text'] = f'Actor:  {actors}'

### CREATE WINDOW
window = Tk()
window.title('Demo Combobox')
window.geometry('500x400')

### CREATE WIDGET
lbl_title = Label(window, text = 'Select your favorite movie: ')
lbl_title.grid(row=0, column=0, columnspan=2, sticky=W)



cbb_movie = Combobox(window, value = movies_list)
cbb_movie.grid(row=1, column=0, columnspan=2, sticky=W)
cbb_movie.bind('<<ComboboxSelected>>', cbb_movie_selected)

lbl_info = Label(window, text = 'Movie info: ')
lbl_info.grid(row=2, column=0, sticky=W)

lbl_director = Label(window, text ='Director: ')
lbl_director.grid(row=3, column=0, columnspan=2, sticky=W)

lbl_actors = Label(window, text = 'Actors: ')
lbl_actors.grid(row=4, column=0, columnspan=2, sticky=W)

window.mainloop()