import sys
import os
from tkinter import *
window=Tk()

window.title('Games')
window.geometry("700x300+10+10")

def MemoryGame():
    os.system('MemoryGame.py')

def SlidingPuzzle():
    os.system('SlideGame.py')

def Tetries():
    os.system('tetries2.py')
    

btn=Button(window, text="Memory Game", fg='blue',command=MemoryGame)
btn.place(x=100, y=150)

btn=Button(window, text="Sliding Puzzle", fg='blue',command=SlidingPuzzle)
btn.place(x=300, y=150)

btn=Button(window, text="Tetries", fg='blue',command=Tetries)
btn.place(x=500, y=150)

lbl=Label(window, text="Welcome to Gaming Zone", fg='red', font=("Helvetica", 16))
lbl.place(x=225, y=50)

window.mainloop()
