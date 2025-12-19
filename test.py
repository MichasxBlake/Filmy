# Source - https://stackoverflow.com/a
# Posted by martineau, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-18, License - CC BY-SA 4.0

from tkinter import *

window = Tk()

rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

window.mainloop()
