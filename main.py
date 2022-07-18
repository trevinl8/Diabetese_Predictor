import tkinter as tk
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Diabetes Predictor')
canvas = tk.Canvas(root, height=700, width=700, bg="#7DD3FC")
canvas.pack()

frame = tk.Frame(root, bg="#BAE6FD")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

Title_label = ttk.Label(root, text="Diabetes Predictor")
Title_label.place(x=340, y=20)

root.mainloop()