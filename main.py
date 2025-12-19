from tkinter import *
import csv


#główne ustawienia początkowe głównego okna
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
    csv_reader = csv.DictReader(file)  

    data_list = []  # Main lista filmów
    for row in csv_reader:
        data_list.append(row)

file.close()

#print(data_list[1]['Tytuł'])

def aktorzy(aktorzy, tytul):
    nowe_okno_2 = Tk()
    nowe_okno_2.title(f"Aktorzy - {tytul}")
    nowe_okno_2.geometry('%dx%d+%d+%d' % (400, 300, x, y))
    nowe_okno_2.configure(background="gray25")

    label_tytul = Label(nowe_okno_2, text=(f"Aktorzy - {tytul}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=50, height=1,).pack()
    label_aktorzy = Label(nowe_okno_2, text=(f"{aktorzy}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=50, height=15,).pack()
    

def Wyswietl():
    a= 0
    b= 0

    nowe_okno_1 = Tk()
    nowe_okno_1.title("Wyświetlanie Filmów")
    nowe_okno_1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    nowe_okno_1.configure(background="gray25")

    frame = Frame(nowe_okno_1)
    frame.grid(row=0, column=0, sticky="nsew")

    canvas = Canvas(frame)
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = Frame(canvas)

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))



    a = 0
    for j in data_list[a]:
        a += 1
        head = Label(content_frame, text=(f"{j}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=24, height=2,).grid(row=0, column=a, sticky="nsew")
    for i in data_list:
        b += 1
        a = 0
        for j in i:
            a += 1
            if j == 'Aktorzy':
                more =Button(content_frame, text="Więcej", font=('Helvetica',9), fg="gray47", background="gray17", width=10, height=2, command=lambda i=i: aktorzy(i['Aktorzy'], i['Tytuł'])).grid(row=b, column=a, sticky="nsew")
            else:
                info = Label(content_frame, text=(f"{i[j]}"), font=('Helvetica',9), fg="gray47", background="gray17", width=27, height=2,).grid(row=b, column=a, sticky="nsew")

    nowe_okno_1.columnconfigure(0, weight=1)
    nowe_okno_1.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

            

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

