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



    #tytuł
    one_label = Label(nowe_okno4, text="Tytuł:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=0, column=0, padx=10, sticky=W)

    myEntry_entry1 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=0, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Tytuł")).grid(row=0, column=2, sticky=W,padx=30)

    #Reżyser
    dwu_label = Label(nowe_okno4, text="Reżyser:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=1, column=0, padx=10, sticky=W)

    myEntry_entry2 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=1, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Reżyser")).grid(row=1, column=2, sticky=W,padx=30)

    #Aktorzy
    trzy_label = Label(nowe_okno4, text="Aktorzy:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=2, column=0, padx=10, sticky=W)

    myEntry_entry3 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=2, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Aktorzy")).grid(row=2, column=2, sticky=W,padx=30)

    #Rok
    cztery_label = Label(nowe_okno4, text="Rok Wydania:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=3, column=0, padx=10, sticky=W)
    myEntry_entry4 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=3, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Rok Wydania")).grid(row=3, column=2, sticky=W,padx=30)

    #Gatunek
    piec_label = Label(nowe_okno4, text="Gatunek:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=4, column=0, padx=10, sticky=W)
    myEntry_entry5 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=4, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Gatunek")).grid(row=4, column=2, sticky=W,padx=30)

    #Średnia Ocena
    szesc_label = Label(nowe_okno4, text="Średnia Ocena:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=5, column=0, padx=10, sticky=W)
    myEntry_entry6 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=5, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Średnia Ocena")).grid(row=5, column=2, sticky=W,padx=30)

    #Liczba Ocen
    siedem_label = Label(nowe_okno4, text="Liczba Ocen:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=6, column=0, padx=10, sticky=W)
    myEntry_entry7 = Entry(nowe_okno4, textvariable=user, width=40).grid(row=6, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Liczba Ocen")).grid(row=6, column=2, sticky=W,padx=30)