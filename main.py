from tkinter import *
import csv

#główne ustawenia
app = Tk()
app.title = ("Filmy")
app.geometry("1400x1000")
app.configure(background="gray17")

#działania

with open('filmy.csv', mode='r',encoding='UTF-8') as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    data_list = []  # List to store dictionaries
    for row in csv_reader:
        data_list.append(row)

#print(data_list[1]['Tytuł'])
    

def Wyswietl():
    nowe_okno_1 = Tk()
    nowe_okno_1.title("Wyświetlanie Filmów")
    nowe_okno_1.geometry("1000x700")
    nowe_okno_1.configure(background="gray25")
    info = Label(nowe_okno_1, text=("\n".join(str.split(repr(data_list)))), font=('Helvetica',1), fg="gray47", background="gray17").pack()

def Wyjscie():
    app.quit()


#ustawienia wyglądu
tytul = Label(app, text="Biblioteka Filmów", font=('Helvetica',50), fg="gray47", background="gray17")
wyswietlanie = Label(app, textvariable=data_list)

show_button = Button(app, text="Wyświetl Wszystkie Filmy", width=40, height=6, command=Wyswietl)
sort_button = Button(app, text="Sortuj po:", width=40, height=6, command=Wyswietl)
filtr_button = Button(app, text="Filtruj po:", width=40, height=6, command=Wyswietl)
add_button = Button(app, text="Dodaj nowy film", width=40, height=6, command=Wyswietl)
delate_button = Button(app, text="Usuń film", width=40, height=6, command=Wyswietl)
edit_button = Button(app, text="Edytuj Film", width=40, height=6, command=Wyswietl)
quit_button = Button(app, text="Wyjdź", width=40, height=6, command=Wyjscie)





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

