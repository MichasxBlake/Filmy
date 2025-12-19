from tkinter import *
import csv

#główne ustawenia
app = Tk()
app.title = ("Filmy")
w = 1400
h = 1000

ws = app.winfo_screenwidth() 
hs = app.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.configure(background="gray17")

#działania

with open('filmy.csv', mode='r',encoding='UTF-8') as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    data_list = []  # List to store dictionaries
    for row in csv_reader:
        data_list.append(row)

#print(data_list[1]['Tytuł'])
    

def Wyswietl():
    a= 0
    b= 0

    nowe_okno_1 = Tk()
    nowe_okno_1.title("Wyświetlanie Filmów")
    nowe_okno_1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    nowe_okno_1.configure(background="gray25")

    a = 0
    for j in data_list[a]:
        a += 1
        head = Label(nowe_okno_1, text=(f"{j}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=24, height=2,).grid(row=0, column=a)
    for i in data_list:
        b += 1
        a = 0
        for j in i:
            a += 1
            info = Label(nowe_okno_1, text=(f"{i[j]}"), font=('Helvetica',9), fg="gray47", background="gray17", width=27, height=2,).grid(row=b, column=a)
            

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

