import tkinter as tk 
from tkinter import messagebox
import joblib

model=joblib.load(r"C:\Users\ADMIN\3D Objects\LAB\compactibility_model.pkl")
def predict():
    try:
        chats=int(chats_entry.get())
        interests=int(interests_entry.get())
        personality=int(personality_entry.get())

        prediction=model.predict([[interests,personality,chats]])
        score=prediction[0]
        if score>=80:
            message="❤️ Perfect Match!"
            colour="#00ff62"
        elif score>=60:
            message="😊 Looks Promising!"
            colour="#00ff99"
        elif score>=40:
            message="🙂 Could Work!"
            colour="#00eaff"
        else:
            message="💔 Better Stay Friends!"
            colour="#ff4444"
        result_label.config(
            text=f"compactibility:{score}%:{message}",
            fg=colour
        )
    except ValueError:
        messagebox.showerror("error","retry the values")
def clear():
    chats_entry.delete(0,tk.END)
    interests_entry.delete(0,tk.END)
    personality_entry.delete(0,tk.END)
    result_label.config(text="",
    fg="white")



root=tk.Tk()
root.title("❤️ Crush Compatibility Predictor ❤️")
root.geometry("450x430")
root.configure(bg="#1a001a")
title=tk.Label(root,
               text="❤️ Crush Compatibility Predictor ❤️",
               font=("arial",14,"bold"),
               fg="#1a001a",
               bg="#ff66ff"
)
title.pack(pady=15)
tk.Label(root,
         text="Daily chats",
         font=("arial",10),
         fg="white",
         bg="#1a001a").pack()
chats_entry=tk.Entry(root,width=25)
chats_entry.pack(pady=10)
tk.Label(root,
         text="Personality match(0-100)",
         fg="white",
         bg="#1a001a").pack()
personality_entry=tk.Entry(root,width=25)
personality_entry.pack(pady=10)
tk.Label(root,
         text="interests coinciding",
         font=("arial",10),
         bg="#1a001a",
         fg="white").pack()
interests_entry=tk.Entry(root,width=25)
interests_entry.pack()
predict_button=tk.Button(root,
                         text="Predict",
                         font=("arial",12,"bold"),
                         fg="white",
                         bg="#800080",
                         command=predict)
predict_button.pack(pady=15)
clear_button=tk.Button(root,text="clear",
                       font=("arial",12,"bold"),
                       fg="white",
                       bg="#444444",
                       command=clear)
clear_button.pack(pady=15)
result_label=tk.Label(root,
                      text="",
                      font=("arial",12,"bold"),
                      fg="white",
                      bg="#1a001a")
result_label.pack(pady=15)

root.mainloop()
