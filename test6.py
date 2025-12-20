from tkinter import *
import csv


#główne ustawienia początkowe głównego okna
app = Tk()
app.title = ("Filmy")

            

def Wyjscie():
    app.quit()

def test():
    new = Toplevel(app)
    new.title("Testowe Okno")



show_button = Button(app, text="Wyświetl Wszystkie Filmy", width=40, height=6, command=test)
sort_button = Button(app, text="Sortuj po:", width=40, height=6, command=Wyjscie)
filtr_button = Button(app, text="Filtruj po:", width=40, height=6, command=Wyjscie)
add_button = Button(app, text="Dodaj nowy film", width=40, height=6, command=Wyjscie)
delate_button = Button(app, text="Usuń film", width=40, height=6, command=Wyjscie)
edit_button = Button(app, text="Edytuj Film", width=40, height=6, command=Wyjscie)
quit_button = Button(app, text="Wyjdź", width=40, height=6, command=Wyjscie)





#wyświetlanie
show_button.pack()
sort_button.pack()
filtr_button.pack()
add_button.pack()
delate_button.pack()
edit_button.pack()
quit_button.pack(side=RIGHT)

app.mainloop()

