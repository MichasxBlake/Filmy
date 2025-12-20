from tkinter import *
import csv


#główne ustawienia początkowe głównego okna
app = Tk()
app.title("Filmy")

main_color = "gray17"

w = 1400
h = 1000

ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.configure(background=f"{main_color}")

#działania

with open('filmy.csv', mode='r',encoding='UTF-8') as file:
    csv_reader = csv.DictReader(file)  

    data_list = []  # Main lista filmów
    for row in csv_reader:
        data_list.append(row)

file.close()

#print(data_list[1]['Tytuł'])
    

def Wyswietl(sortuj_po=None, filtruj_po=None, filtr=None):
    a= 0
    b= 0

    nowe_okno_1 = Toplevel(app)
    nowe_okno_1.title("Wyświetlanie Filmów")
    nowe_okno_1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    nowe_okno_1.configure(background=f"{main_color}")

    frame = Frame(nowe_okno_1)
    frame.grid(row=0, column=0, sticky="nsew")

    canvas = Canvas(frame, background=f"{main_color}")
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = Frame(canvas)

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    if sortuj_po:
        data_list.sort(key=lambda x: x[sortuj_po])
    if filtruj_po:
        expectedResult = [d for d in data_list if d[filtruj_po] in filtr]
        

    if filtruj_po:
        end_data_list = expectedResult
    else:
        end_data_list = data_list

    a = 0
    for j in end_data_list[a]:
        a += 1
        head = Label(content_frame, text=(f"{j}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=24, height=2,).grid(row=0, column=a, sticky="nsew")
    for i in end_data_list:
        b += 1
        a = 0
        for j in i:
            a += 1
            if j == 'Aktorzy':
                more =Button(content_frame, text="Więcej", font=('Helvetica',9), fg="gray47", background=f"{main_color}", width=10, height=2, command=lambda i=i: aktorzy(i['Aktorzy'], i['Tytuł'])).grid(row=b, column=a, sticky="nsew")
            else:
                info = Label(content_frame, text=(f"{i[j]}"), font=('Helvetica',9), fg="gray47", background=f"{main_color}", width=27, height=2).grid(row=b, column=a, sticky="nsew")

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

    def aktorzy(aktorzy, tytul):
        nowe_okno_2 = Toplevel(nowe_okno_1)
        nowe_okno_2.title(f"Aktorzy - {tytul}")
        nowe_okno_2.geometry('%dx%d+%d+%d' % (400, 300, (ws/2) - (400/2), (hs/2) - (300/2)))
        nowe_okno_2.configure(background=f"{main_color}")

        label_tytul = Label(nowe_okno_2, text=(f"Aktorzy - {tytul}"), font=('Helvetica',10,'bold'), fg="gray47", background=f"{main_color}", width=50, height=1,).pack()
        label_aktorzy = Label(nowe_okno_2, text=(f"{aktorzy}"), font=('Helvetica',10,'bold'), fg="gray47", background=f"{main_color}", width=50, height=15,).pack()


def Sortuj():
    nowe_okno_3 = Toplevel(app)
    nowe_okno_3.title("Sortowanie Filmów")
    nowe_okno_3.geometry('%dx%d+%d+%d' % (655, 250, (ws/2) - (400/2), (hs/2) - (300/2)))
    nowe_okno_3.configure(background=f"{main_color}")

    # zrozumieć w pełni jak działają lambda w tym przypadku i innnych XD
    gora = Label(nowe_okno_3, text="Sortuj filmy po:", font=('Helvetica',15,'bold'), fg="gray47", background=f"{main_color}", width=50, height=2,).grid(row=0, column=0, columnspan=7)
    nazwa = Button(nowe_okno_3, text="Nazwa", width=12, height=1, command=lambda : Wyswietl("Tytuł")).grid(row=1, column=0)
    rezyser = Button(nowe_okno_3, text="Reżyser", width=12, height=1, command=lambda : Wyswietl("Reżyser")).grid(row=1, column=1)
    aktorzy1 = Button(nowe_okno_3, text="Aktorzy", width=12, height=1, command=lambda : Wyswietl("Aktorzy")).grid(row=1, column=2)
    rok = Button(nowe_okno_3, text="Rok", width=12, height=1, command=lambda : Wyswietl("Rok wydania")).grid(row=1, column=3)
    gatunek = Button(nowe_okno_3, text="Gatunek", width=12, height=1, command=lambda : Wyswietl("Gatunek")).grid(row=1, column=4)
    srednia = Button(nowe_okno_3, text="Średnia Ocena", width=12, height=1, command=lambda : Wyswietl("Średnia Ocena")).grid(row=1, column=5)
    liczba = Button(nowe_okno_3, text="Liczba Ocen", width=12, height=1, command=lambda : Wyswietl("Liczba Ocen")).grid(row=1, column=6)
    

def Filtruj():
    def on_button(filtruj_po=None, myValue=None):
        Wyswietl(filtruj_po=filtruj_po, filtr=myValue)
        

    nowe_okno4 = Toplevel(app)
    nowe_okno4.title("Sortowanie Filmów")
    nowe_okno4.geometry('%dx%d+%d+%d' % (655, 350, (ws/2) - (400/2), (hs/2) - (300/2)))
    nowe_okno4.configure(background=f"{main_color}")

    
    #tytuł
    one_label = Label(nowe_okno4, text="Tytuł:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=0, column=0, padx=10, sticky=W)
    user1 = StringVar()
    myEntry_entry1 = Entry(nowe_okno4, textvariable=user1, width=40).grid(row=0, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Tytuł", user1.get())).grid(row=0, column=2, sticky=W,padx=30)

    #Reżyser
    dwu_label = Label(nowe_okno4, text="Reżyser:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=1, column=0, padx=10, sticky=W)
    user2 = StringVar()
    myEntry_entry2 = Entry(nowe_okno4, textvariable=user2, width=40).grid(row=1, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Reżyser", user2.get())).grid(row=1, column=2, sticky=W,padx=30)

    #Aktorzy
    trzy_label = Label(nowe_okno4, text="Aktorzy:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=2, column=0, padx=10, sticky=W)
    user3 = StringVar()
    myEntry_entry3 = Entry(nowe_okno4, textvariable=user3, width=40).grid(row=2, column=1, sticky=W, padx=10)

    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Aktorzy", user3.get())).grid(row=2, column=2, sticky=W,padx=30)

    #Rok
    cztery_label = Label(nowe_okno4, text="Rok Wydania:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=3, column=0, padx=10, sticky=W)
    user4 = StringVar()
    myEntry_entry4 = Entry(nowe_okno4, textvariable=user4, width=40).grid(row=3, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Rok wydania", user4.get())).grid(row=3, column=2, sticky=W,padx=30)

    #Gatunek
    piec_label = Label(nowe_okno4, text="Gatunek:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=4, column=0, padx=10, sticky=W)
    user5 = StringVar()
    myEntry_entry5 = Entry(nowe_okno4, textvariable=user5, width=40).grid(row=4, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Gatunek", user5.get())).grid(row=4, column=2, sticky=W,padx=30)

    #Średnia Ocena
    szesc_label = Label(nowe_okno4, text="Średnia Ocena:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=5, column=0, padx=10, sticky=W)
    user6 = StringVar()
    myEntry_entry6 = Entry(nowe_okno4, textvariable=user6, width=40).grid(row=5, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Średnia Ocena", user6.get())).grid(row=5, column=2, sticky=W,padx=30)

    #Liczba Ocen
    siedem_label = Label(nowe_okno4, text="Liczba Ocen:", font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=16, height=2,).grid(row=6, column=0, padx=10, sticky=W)
    user7 = StringVar()
    myEntry_entry7 = Entry(nowe_okno4, textvariable=user7, width=40).grid(row=6, column=1, sticky=W, padx=10)
    button1 = Button(nowe_okno4, text="Szukaj", command=lambda : on_button("Liczba Ocen", user7.get())).grid(row=6, column=2, sticky=W,padx=30)

            

def Wyjscie():
    app.quit()




#ustawienia wyglądu
tytul = Label(app, text="Biblioteka Filmów", font=('Helvetica',50), fg="gray47", background="gray17")
wyswietlanie = Label(app, textvariable=data_list)

show_button = Button(app, text="Wyświetl Wszystkie Filmy", width=40, height=6, command=Wyswietl)
sort_button = Button(app, text="Sortuj po:", width=40, height=6, command=Sortuj)
filtr_button = Button(app, text="Filtruj po:", width=40, height=6, command=Filtruj)
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

