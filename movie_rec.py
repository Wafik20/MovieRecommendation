import tkinter as tk
import logic
from tkinter import *
OPTIONS = logic.titles
master = tk.Tk(className=' Get Your Movie Recommendation')
master.geometry("800x400")
variable = tk.StringVar(master)
variable.set(OPTIONS[0]) # default value
text_box = Text(master, height = 20, width = 70)


w = OptionMenu(master, variable, *OPTIONS)
w.pack()
def ok():
    text_box.delete("1.0","end")
    movie = variable.get()
    recommendation = logic.get_recommendations(movie)
    print(recommendation)
    text_box.insert(tk.END,recommendation)


button = Button(master, text="Get movies recommendations", command=ok)
button.pack()
text_box.pack(expand=True)



mainloop()
