#Importy
from tkinter import *
import csv

#zmienne

main_color = "gray17"

ilosc_nowych = 0

czy_usunieto = False

#główne ustawienia początkowe głównego okna
app = Tk()
app.title("Filmy")
w = 1400
h = 1000
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.configure(background=f"{main_color}")

#Pobieranie danych z pliku

with open('filmy.csv', mode='r',encoding='UTF-8') as file:
    csv_reader = csv.DictReader(file)  

    data_list = []  # Main lista filmów
    for row in csv_reader:
        data_list.append(row)
    for d in data_list:   # rozbicie bo tam jest ich kilka
        if d['Aktorzy']:
            d['Aktorzy'] = d['Aktorzy'].split('; ')
        if d['Reżyser']:
            d['Reżyser'] = d['Reżyser'].split('; ')

file.close()

#print(data_list[1]['Tytuł'])
    
#główna funkcja wyświetlania, na której wszystko bazuje

def Wyswietl(sortuj_po=None, filtruj_po=None, filtr=None, czy_usuwanie=False, czy_edycja=False, czy_ocena=False):

    #zmienne w funkcji
    a= 0
    b= 0
    powtorka = False

    #różne ustawienia dla różnych działań

    if czy_usuwanie:
        nowe_okno_1 = Toplevel(app)
        nowe_okno_1.title("Usuwanie Filmów")
        nowe_okno_1.geometry('%dx%d+%d+%d' % (w+200, h, x, y))
        nowe_okno_1.configure(background=f"{main_color}")

    elif czy_edycja:
        nowe_okno_1 = Toplevel(app)
        nowe_okno_1.title("Edycja Filmów")
        nowe_okno_1.geometry('%dx%d+%d+%d' % (w+200, h, x, y))
        nowe_okno_1.configure(background=f"{main_color}")

    elif czy_ocena:
        nowe_okno_1 = Toplevel(app)
        nowe_okno_1.title("Ocenianie Filmów")
        nowe_okno_1.geometry('%dx%d+%d+%d' % (w+200, h, x, y))
        nowe_okno_1.configure(background=f"{main_color}")
        
    else: #główne okno 
        nowe_okno_1 = Toplevel(app)
        nowe_okno_1.title("Wyświetlanie Filmów")
        nowe_okno_1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        nowe_okno_1.configure(background=f"{main_color}")


    #ustanienie scroll-a jak za dużo filmów
    frame = Frame(nowe_okno_1)
    frame.grid(row=0, column=0, sticky="nsew")

    canvas = Canvas(frame, background=f"{main_color}")
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = Frame(canvas)

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

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


    #funkcja sortowania
    if sortuj_po:
        data_list.sort(key=lambda x: x[sortuj_po])


    #filtrowanie (podzielone na opcjie, z obu wychodzą inne też)

    # wersja dla aktorów    
    if filtruj_po:
        if filtruj_po == "Aktorzy":
            for d in data_list:
                for actor in d['Aktorzy']:
                    if actor == filtr:
                        if 'expectedResult' not in locals():
                            expectedResult = []
                        expectedResult.append(d)
                    elif 'expectedResult' not in locals():
                        expectedResult = []

        else:
            if filtruj_po != "Reżyser":
                expectedResult = [d for d in data_list if d[filtruj_po] in filtr]
                powtorka = True


    #wersja dla reżyserów
    if filtruj_po:
        if filtruj_po == "Reżyser":
                for d in data_list:
                    for director in d['Reżyser']:
                        if director == filtr:
                            if 'expectedResult' not in locals():
                                expectedResult = []
                            expectedResult.append(d)
                        elif 'expectedResult' not in locals():
                            expectedResult = []

        else:
            if powtorka == True:
                expectedResult = [d for d in data_list if d[filtruj_po] in filtr]


    #po filtrze końcowe ustawianie wyświetlacza
    if filtruj_po:
        end_data_list = expectedResult
    else:
        end_data_list = data_list


    #Funkcja usuwająca
    def Lokacja(place = None):
        place = place['Tytuł']

        Usuwanie(True, tytul=f"{place}")

    #główna część od wyświetlania danych (zbiera informacje do wyświetlenia)

    try:
        for j in end_data_list[a]: #najprostrze wyświetlanie 
            a += 1
            head1 = Label(content_frame, text=(f"{j}"), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=24, height=2,).grid(row=0, column=a, sticky="nsew")
            korekta = Label(content_frame, text=(""), font=('Helvetica',10,'bold'), fg="gray47", background="gray17", width=10, height=2,).grid(row=0, column=a+1, sticky="nsew") #to przez guziki
    except IndexError:
        head2 = Label(content_frame, text=("Brak wyników do wyświetlenia"), font=('Helvetica',40,'bold'), fg="gray47", background="gray17", width=44, height=12,).grid(row=1, column=1, sticky="nsew") #jak nic nie ma
    for i in end_data_list: #dodatek bo aktorów jest wielu
        b += 1
        a = 0
        for j in i:
            a += 1
            if j == 'Aktorzy':
                more = Button(content_frame, text="Więcej", font=('Helvetica',9), fg="gray47", background=f"{main_color}", width=10, height=2, command=lambda i=i: aktorzy(i['Aktorzy'], i['Tytuł'])).grid(row=b, column=a, sticky="nsew")
            else:
                info = Label(content_frame, text=(f"{i[j]}"), font=('Helvetica',9), fg="gray47", background=f"{main_color}", width=27, height=2).grid(row=b, column=a, sticky="nsew")
        # dodatkowe ustawienia dla innych działań (guziki)
        if czy_usuwanie:
            delete = Button(content_frame, text="Usuń", background="dim gray", width=10, height=2, command=lambda i=i : Lokacja(i)).grid(row=b, column=a+1)
        elif czy_edycja:
                edit = Button(content_frame, text="Edytuj", background="dim gray", width=10, height=2, command=lambda i=i : Edycja(i)).grid(row=b, column=a+1)
        elif czy_ocena:
                star = Button(content_frame, text="Oceń", background="dim gray", width=10, height=2, command=lambda i=i : Ocena(i)).grid(row=b, column=a+1)

    #te okno od aktorów
    def aktorzy(aktorzy, tytul):
        nowe_okno_2 = Toplevel(nowe_okno_1)
        nowe_okno_2.title(f"Aktorzy - {tytul}")
        nowe_okno_2.geometry('%dx%d+%d+%d' % (400, 300, (ws/2) - (400/2), (hs/2) - (300/2)))
        nowe_okno_2.configure(background=f"{main_color}")

        label_tytul = Label(nowe_okno_2, text=(f"Aktorzy - {tytul}"), font=('Helvetica',10,'bold'), fg="gray47", background=f"{main_color}", width=50, height=1,).pack()
        label_aktorzy = Label(nowe_okno_2, text=(f"{aktorzy}"), font=('Helvetica',10,'bold'), fg="gray47", background=f"{main_color}", width=50, height=15,).pack()
#Koniec wyświetlania

#funkcja sortująca
def Sortuj():
    #okno
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
    
#funkcja filtrująca
def Filtruj(czy_usuwanie=False):

    #działanie przycisków + funkcja usuwania
    def on_button(filtruj_po=None, myValue=None):
        nonlocal czy_usuwanie
        Wyswietl(filtruj_po=filtruj_po, filtr=myValue, czy_usuwanie=czy_usuwanie)
        #usuwanie
        if czy_usuwanie:
            nowe_okno4.destroy()
        
    #ustawienia
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


#funkcja dodawania
def Dodawaj():

    #okno
    nowe_okno_5 = Toplevel(app)
    nowe_okno_5.title(" Dodaj Nowy Film")
    nowe_okno_5.geometry('%dx%d+%d+%d' % (655, 350, (ws/2) - (400/2), (hs/2) - (300/2)))
    nowe_okno_5.configure(background=f"{main_color}")

    #funkcja
    def Add():
        new_movie = {
            'Tytuł': new_title.get(),
            'Reżyser': new_director.get(),
            'Aktorzy': new_actors.get(),
            'Rok wydania': new_year.get(),
            'Gatunek': new_tag.get(),
            'Średnia Ocena': '0',
            'Liczba Ocen': '0'
        }
        data_list.append(new_movie)
        nowe_okno_5.destroy()

    #pure text

    gora2 = Label(nowe_okno_5, text="Dodaj Nowy Film:", font=('Helvetica',15,'bold'), fg="gray47", background=f"{main_color}", width=55, height=2,).grid(row=0, column=0, columnspan=7)
    gora3 = Label(nowe_okno_5, text="Tytuł:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=9, column=0)
    gora3 = Label(nowe_okno_5, text="Reżyser:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=10, column=0)
    gora3 = Label(nowe_okno_5, text="Aktorzy:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=11, column=0)
    gora3 = Label(nowe_okno_5, text="Rok Wydania:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=12, column=0)
    gora3 = Label(nowe_okno_5, text="Gatunek:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=13, column=0)
    new_title = StringVar()
    new_director = StringVar()
    new_actors = StringVar()
    new_year = StringVar()
    new_tag = StringVar()
    nowy_tytul = Entry(nowe_okno_5, textvariable=new_title, width=40).grid(row=9, column=1, sticky=W, padx=1)
    nowy_rezyser = Entry(nowe_okno_5, textvariable=new_director, width=40).grid(row=10, column=1, sticky=W, padx=1)
    nowy_actorzy = Entry(nowe_okno_5, textvariable=new_actors, width=40).grid(row=11, column=1, sticky=W, padx=1)
    nowy_rok = Entry(nowe_okno_5, textvariable=new_year, width=40).grid(row=12, column=1, sticky=W, padx=1)
    nowy_gatunek = Entry(nowe_okno_5, textvariable=new_tag, width=40).grid(row=13, column=1, sticky=W, padx=1)
    button1 = Button(nowe_okno_5, text="Dodaj", command=Add, width=10, height=4, background="dim gray").grid(row=20, column=1, sticky=W, padx=80)

#funkcja usuwanie
def Usuwanie(tak= False, tytul=None):

    #końcowe działanie
    if tak:
        data_list.remove(next(item for item in data_list if item["Tytuł"] == tytul))
        global czy_usunieto
        czy_usunieto = True
        #skok do filtra
    else:
        Filtruj(czy_usuwanie=True)

#funkcja edycja
def Edycja(i=None):
    
    #główne działanie
    if i:
        nowe_okno_6 = Toplevel(app)
        nowe_okno_6.title(" Edytuj Film")
        nowe_okno_6.geometry('%dx%d+%d+%d' % (655, 350, (ws/2) - (400/2), (hs/2) - (300/2)))
        nowe_okno_6.configure(background=f"{main_color}")

        #zapis
        def Save():
            i['Tytuł'] = edit_title.get()
            i['Reżyser'] = edit_director.get()
            i['Aktorzy'] = edit_actors.get()
            i['Rok wydania'] = edit_year.get()
            i['Gatunek'] = edit_tag.get()
            nowe_okno_6.destroy()

        #pure text
        edit_title = StringVar(value=i['Tytuł'])
        edit_director = StringVar(value=i['Reżyser'])
        edit_actors = StringVar(value=i['Aktorzy'])
        edit_year = StringVar(value=i['Rok wydania'])
        edit_tag = StringVar(value=i['Gatunek'])
        gora2 = Label(nowe_okno_6, text="Edytuj Film:", font=('Helvetica',15,'bold'), fg="gray47", background=f"{main_color}", width=55, height=2,).grid(row=0, column=0, columnspan=7)
        gora3 = Label(nowe_okno_6, text="Tytuł:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=9, column=0)
        gora4 = Label(nowe_okno_6, text="Reżyser:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=10, column=0)
        gora5 = Label(nowe_okno_6, text="Aktorzy:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=11, column=0)
        gora6 = Label(nowe_okno_6, text="Rok Wydania:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=12, column=0)
        gora7 = Label(nowe_okno_6, text="Gatunek:", font=('Helvetica',11,'bold'), fg="gray47", background=f"{main_color}", width=0, height=2,).grid(row=13, column=0)
        edytuj_tytul = Entry(nowe_okno_6, textvariable=edit_title, width=40).grid(row=9, column=1, sticky=W, padx=1)
        edytuj_rezyser = Entry(nowe_okno_6, textvariable=edit_director, width=40).grid(row=10, column=1, sticky=W, padx=1)
        edytuj_actorzy = Entry(nowe_okno_6, textvariable=edit_actors, width=40).grid(row=11, column=1, sticky=W, padx=1)
        edytuj_rok = Entry(nowe_okno_6, textvariable=edit_year, width=40).grid(row=12, column=1, sticky=W, padx=1)
        edytuj_gatunek = Entry(nowe_okno_6, textvariable=edit_tag, width=40).grid(row=13, column=1, sticky=W, padx=1)
        button1 = Button(nowe_okno_6, text="Zapisz", command=Save, width=10, height=4, background="dim gray").grid(row=20, column=1, sticky=W, padx=80)
        
    #przechodzenie do wyświetlacza
    else:
        Wyswietl(czy_edycja=True)


#funkcja oceniajaca
def Ocena(i=None):

    #główne działanie
    if i:
        nowe_okno_7 = Toplevel(app)
        nowe_okno_7.title(" Oceń Film")
        nowe_okno_7.geometry('%dx%d+%d+%d' % (655, 350, (ws/2) - (400/2), (hs/2) - (300/2)))
        nowe_okno_7.configure(background=f"{main_color}")

        #ustawianie i obliczanie oceny
        def rate(stars):
            srednia = float(i['Średnia Ocena'])
            liczba = int(i['Liczba Ocen'])

            new_count = liczba + 1
            new_average = ((srednia * liczba) + stars) / new_count
            i['Średnia Ocena'] = f"{new_average:.2f}"
            i['Liczba Ocen'] = str(new_count)

            nowe_okno_7.destroy()

        head = Label(nowe_okno_7, text="Oceń Film:", font=('Helvetica',15,'bold'), fg="gray47", background=f"{main_color}", width=55, height=2,).grid(row=0, column=0, columnspan=7)
        button_1 = Button(nowe_okno_7, text="1", width=10, height=4, background="dim gray", command=lambda: rate(1)).grid(row=1, column=0, padx=10)
        button_2 = Button(nowe_okno_7, text="2", width=10, height=4, background="dim gray", command=lambda: rate(2)).grid(row=1, column=1, padx=10)
        button_3 = Button(nowe_okno_7, text="3", width=10, height=4, background="dim gray", command=lambda: rate(3)).grid(row=1, column=2, padx=10)
        button_4 = Button(nowe_okno_7, text="4", width=10, height=4, background="dim gray", command=lambda: rate(4)).grid(row=1, column=3, padx=10)
        button_5 = Button(nowe_okno_7, text="5", width=10, height=4, background="dim gray", command=lambda: rate(5)).grid(row=1, column=4, padx=10)
        button_6 = Button(nowe_okno_7, text="6", width=10, height=4, background="dim gray", command=lambda: rate(6)).grid(row=1, column=5, padx=10)
        button_7 = Button(nowe_okno_7, text="7", width=10, height=4, background="dim gray", command=lambda: rate(7)).grid(row=1, column=6, padx=10)
        button_8 = Button(nowe_okno_7, text="8", width=10, height=4, background="dim gray", command=lambda: rate(8)).grid(row=2, column=0, padx=10)
        button_9 = Button(nowe_okno_7, text="9", width=10, height=4, background="dim gray", command=lambda: rate(9)).grid(row=2, column=1, padx=10)
        button_10 = Button(nowe_okno_7, text="10", width=10, height=4, background="dim gray", command=lambda: rate(10)).grid(row=2, column=2, padx=10)

    #skok wyświelacz
    else:
        Wyswietl(czy_ocena=True)

            
#koniec
def Wyjscie():

    #przywrócienie listy do tego co było w pliku *to był koszmar*
    for d in data_list:
        if isinstance(d['Aktorzy'], list):
            d['Aktorzy'] = '; '.join(d['Aktorzy'])
        if isinstance(d['Reżyser'], list):
            d['Reżyser'] = '; '.join(d['Reżyser'])

    #zapis do pliku
    keys = data_list[0].keys() if data_list else []
    with open('filmy.csv', 'w', newline='', encoding='UTF-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
    app.quit()




#główny wygląd menu aplikacji
tytul = Label(app, text="Biblioteka Filmów", font=('Helvetica',50), fg="gray47", background="gray17")
wyswietlanie = Label(app, textvariable=data_list)

show_button = Button(app, text="Wyświetl Wszystkie Filmy", width=40, height=6, command=Wyswietl).pack()
sort_button = Button(app, text="Sortuj po:", width=40, height=6, command=Sortuj).pack()
filtr_button = Button(app, text="Filtruj po:", width=40, height=6, command=Filtruj).pack()
add_button = Button(app, text="Dodaj nowy film", width=40, height=6, command=Dodawaj).pack()
delate_button = Button(app, text="Usuń film", width=40, height=6, command=Usuwanie).pack()
edit_button = Button(app, text="Edytuj Film", width=40, height=6, command=Edycja).pack()
star_button = Button(app, text="Oceń Film", width=40, height=6, command=Ocena).pack()
quit_button = Button(app, text="Wyjdź", width=40, height=6, command=Wyjscie).pack(side=RIGHT)


#Start aplikacji
app.mainloop()

