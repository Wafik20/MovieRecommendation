from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
import logic

countries = logic.titles

ws = Tk()
ws.title('Movie Recommendations')
ws.geometry('600x400')
ws.config(bg='#8DBF5A')

frame = Frame(ws, bg='#8DBF5A')
frame.pack(expand=True)

Label(
    frame, 
    bg='#8DBF5A',
    font = ('Times',21),
    text='Enter Movie : '
    ).pack()
    
entry = AutocompleteCombobox(
    frame, 
    width=30, 
    font=('Times', 18),
    completevalues=countries
    )
def print_rec():
    text_box.delete("1.0","end")
    movie = entry.get()
    recommendation = logic.get_recommendations(movie)
    print(recommendation)
    text_box.insert(END,recommendation)
button = Button(ws, text="Get movies recommendations", command=print_rec)
entry.pack()
button.pack()
text_box = Text(ws, height = 20, width = 70)
text_box.pack()
ws.mainloop()   