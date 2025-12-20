from tkinter import *

win = Tk()

for row in range(3):
    for col in range(3):
        Label(win, text=f'{row}x{col}').grid(row=row,column=col)

for widget in win.grid_slaves(1, 2):
    print(widget['text'])

print("---------------------------------")
mama  = win.grid_slaves(0,2)
print(mama[0]['text'])

win.mainloop()