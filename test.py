# Source - https://stackoverflow.com/a
# Posted by martineau, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-18, License - CC BY-SA 4.0

from tkinter import *

window = Tk()

grades = ["2", "2+","3","3+","4","4+","5","5+","6"]
points = [0.41,0.52,0.54,0.72,0.74,0.85,0.87,0.93,0.97]

def calculate():

    def get_float_value(entry):  # Helper function
        contents = entry.get()
        return 0.0 if not contents else float(contents)

    max_points = [i * get_float_value(e1_value) for i in points]
    max_points = [str(round(i)) for i in max_points]

    t1.delete("1.0", END)  # Clear widget.
    for grade, point in zip(grades, max_points):
        t1.insert(END, f"{grade} do {point} punktów\n")

b1 = Button(window, text="Execute", command=calculate)
b1.grid(row=1, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2 = Label(window, text="Max points")
e2.grid(row=0, column=0)

t1 = Text(window, height=15, width=20)
t1.grid(row=1, column=1)

window.mainloop()
