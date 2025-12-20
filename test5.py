import tkinter as tk
from tkinter import ttk

def on_button():
    myValue = myEntry.get()
    print(myValue)

root = tk.Tk()

w = tk.Frame(root)
w.grid(row=0, columnspan=3)

first_label = tk.Label(w, text="myEntry: ")
first_label.grid(row=0, column=0, padx=10, sticky=tk.W)

myEntry = tk.StringVar()
myEntry_entry = ttk.Entry(w, textvariable=myEntry)
myEntry_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

button1 = tk.Button(w, text="Print in Console", command=on_button)
button1.grid(row=4, columnspan=1, sticky=tk.W)

root.mainloop()



