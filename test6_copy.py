from tkinter import *

def open_new_window():
    # Tworzy nowe okno Toplevel
    new_window = Toplevel(root)
    new_window.title("Nowe Okno")
    new_window.geometry("200x100")

    # Dodaje label do nowego okna
    label = Label(new_window, text="To jest nowe okno!")
    label.pack(pady=20)

    # Ustawia focus na nowe okno, blokując główne
    new_window.grab_set()

# Główny kod aplikacji
root = Tk()
root.title("Główne Okno")
root.geometry("300x200")

# Przycisk do otwierania nowego okna
open_button = Button(root, text="Otwórz nowe okno", command=open_new_window)
open_button.pack(pady=50)

root.mainloop()