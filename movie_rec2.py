from cgitb import text
from sre_parse import State
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
import logic
import numpy as np
import pandas as pd

titles = logic.titles

ws = Tk()
ws.title('Movie Recommendations')
ws.geometry('500x500')
ws.config(bg='#8DBF5A')

frame = Frame(ws, bg='#8DBF5A')
frame.pack(expand=False)

Label(
    frame, 
    bg='#8DBF5A',
    font ='Georgia 20 italic bold',
    text='Enter Movie : '
    ).pack(side=TOP)
    
entry = AutocompleteCombobox(
    frame,
    width=20, 
    font=('Times', 18),
    completevalues=titles
    )
def print_rec():
    text_box.config(state = NORMAL)
    text_box.delete("1.0","end")
    movie = entry.get()
    recommendation = logic.get_recommendations(movie)
    titles = ''
    for i in range(len(recommendation)):
       titles += (str(i+1) + '-' +recommendation[i])
       titles += '\n'
    text_box.insert(END,titles)
    text_box.config(state = DISABLED)
button = Button(ws, text="Get movies recommendations", command=print_rec)
entry.pack(side=TOP)
button.place(in_ = entry, relx = 0.2, rely = 1.2)
text_box = Text(ws, height = 15, width = 30,font='Georgia 14 italic bold',relief='sunken', highlightthickness=1, borderwidth=2)
text_box.place(in_=ws, relx = 0.1, rely = 0.23)
ws.resizable(False,False)
ws.mainloop()   