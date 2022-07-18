import tkinter as tk
from tkinter import Text
import os

root = tk.Tk()
root.title('Diabetes Predictor')
canvas = tk.Canvas(root, height=700, width=700, bg="#7DD3FC")
canvas.pack()

frame = tk.Frame(root, bg="#BAE6FD")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

root.mainloop()