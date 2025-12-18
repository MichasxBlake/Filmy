from tkinter import *

#główne ustawenia
app = Tk()
app.title = ("Filmy")
app.geometry("1400x1000")
app.configure(background="gray17")

def Wyswietl():
    print("wyswietla")


#ustawienia wyglądu
tytul = Label(app, text="Biblioteka Filmów", font=('Helvetica',50), fg="gray47", background="gray17")

show_button = Button(app, text="Wyświetl Wszystkie Filmy", width=40, height=6, command=Wyswietl())
sort_button = Button(app, text="Sortuj po:", width=40, height=6, command=Wyswietl())
filtr_button = Button(app, text="Filtruj po:", width=40, height=6, command=Wyswietl())
add_button = Button(app, text="Dodaj nowy film", width=40, height=6, command=Wyswietl())
delate_button = Button(app, text="Usuń film", width=40, height=6, command=Wyswietl())
edit_button = Button(app, text="Edytuj Film", width=40, height=6, command=Wyswietl())
quit_button = Button(app, text="Wyjdź", width=40, height=6, command=Wyswietl())





#wyświetlanie
tytul.pack()
show_button.pack()
sort_button.pack()
filtr_button.pack()
add_button.pack()
delate_button.pack()
edit_button.pack()
quit_button.pack(side=RIGHT)

app.mainloop()