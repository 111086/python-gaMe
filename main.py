print ("Welkom")
print("Lucifer game")
print ("Je speelt tegen een computer die een getal kiest tussen 20 en 25, om de beurt trekt een speler 1,2 of 3 lucifers weg. De speler die het laatste lucifer trekt," )
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('Lucifer game')

# exit button
start_button = ttk.Button(
    root,
    text='start',
    command=lambda: root.quit()
)

start_button.pack(
    ipadx=100,
    ipady=50,
    expand=True
)

root.mainloop()
    