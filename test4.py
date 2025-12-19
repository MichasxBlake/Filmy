import tkinter as tk


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox(tk.ALL))


root = tk.Tk()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(root)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.configure(command=canvas.yview)

content = tk.Frame(canvas)
content.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

canvas.create_window((0,0), window=content, anchor=tk.NW)


entries = []
for i in range(26):
   tk.Label(content, text=chr(65+i)).grid(row=i, column=0, padx=15)
   tk.Label(content, text=str(i)).grid(row=i, column=1, padx=15)
   e = tk.Entry(content, width=5)
   e.grid(row=i, column=2)
   e.insert(0, "0")
   entries.append(e)


root.mainloop()