import tkinter as tk
import pickle
import pandas as pd
import numpy as np
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Diabetes Predictor')
canvas = tk.Canvas(root, height=700, width=700, bg="#7DD3FC")
canvas.pack()

cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age']

Pregnancies = tk.StringVar()
Glucose = tk.StringVar()
BloodPressure = tk.StringVar()
SkinThickness = tk.StringVar()
Insulin = tk.StringVar()
BMI = tk.StringVar()
DPF = tk.StringVar()
Age = tk.StringVar()

model = pickle.load(open('DPRF_Model.pkl', 'rb'))

def on_predict():
    df = pd.DataFrame(columns=cols)
    df['Pregnancies'] = [float(Pregnancies.get())]
    df['Glucose'] = [float(Glucose.get())]
    df['BloodPressure'] = [float(BloodPressure.get())]
    df['SkinThickness'] = [float(SkinThickness.get())]
    df['Insulin'] = [float(Insulin.get())]
    df['BMI'] = [float(BMI.get())]
    df['DPF'] = [float(DPF.get())]
    df['Age'] = [float(Age.get())]

    pred = model.predict(df)
    label = "has Diabetes" if pred[0] == 1 else "doesn't have Diabetes"
    showinfo(title="Prediction Results", message="This patient: {}".format(label))

frame = tk.Frame(root)
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

Title_label = ttk.Label(root, text="Diabetes Predictor", font='Arial 35')
Title_label.place(x=150, y=80)

Pregnancies_lbl = ttk.Label(root, text="Pregnancies",  font='Arial 15')
Glucose_lbl = ttk.Label(root, text="Glucose",  font='Arial 15')
BloodPressure_lbl = ttk.Label(root, text="Blood Pressure",  font='Arial 15')
SkinThickness_lbl = ttk.Label(root, text="Skin Thickness",  font='Arial 15')
Insulin_lbl = ttk.Label(root, text="Insulin",  font='Arial 15')
BMI_lbl = ttk.Label(root, text="BMI",  font='Arial 15')
DPF_lbl = ttk.Label(root, text="DPF",  font='Arial 15')
Age_lbl = ttk.Label(root, text="Age",  font='Arial 15')

Pregnancies_lbl.place(x=130, y=160)
Glucose_lbl.place(x=130, y=200)
BloodPressure_lbl.place(x=130, y=240)
SkinThickness_lbl.place(x=130, y=280)
Insulin_lbl.place(x=130, y=320)
BMI_lbl.place(x=130, y=360)
DPF_lbl.place(x=130, y=400)
Age_lbl.place(x=130, y=440)

Pregnancies_entry = ttk.Entry(root, textvariable=Pregnancies, width=20,  font='Arial 15')
Glucose_entry = ttk.Entry(root, textvariable=Glucose, width=20,  font='Arial 15')
BloodPressure_entry = ttk.Entry(root, textvariable=BloodPressure, width=20,  font='Arial 15')
SkinThickness_entry = ttk.Entry(root, textvariable=SkinThickness, width=20,  font='Arial 15')
Insulin_entry = ttk.Entry(root, textvariable=Insulin, width=20,  font='Arial 15')
BMI_entry = ttk.Entry(root, textvariable=BMI, width=20, font='Arial 15')
DPF_entry = ttk.Entry(root, textvariable=DPF, width=20,  font='Arial 15')
Age_entry = ttk.Entry(root, textvariable=Age, width=20,  font='Arial 15')

Pregnancies_entry.place(x=330, y=160)
Glucose_entry.place(x=330, y=200)
BloodPressure_entry.place(x=330, y=240)
SkinThickness_entry.place(x=330, y=280)
Insulin_entry.place(x=330, y=320)
BMI_entry.place(x=330, y=360)
DPF_entry.place(x=330, y=400)
Age_entry.place(x=330, y=440)

submit_btn = ttk.Button(root, text="Predict", width=36, command=on_predict)
submit_btn.place(x=330, y=500)

root.mainloop()