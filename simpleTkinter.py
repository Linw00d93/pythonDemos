import tkinter as tk

window = tk.Tk()

entry = tk.Entry()
entry.pack()
frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=1, column=1)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=2, column=1)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=3, column=1)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()
window.columnconfigure(frame, weight=1, minsize=75)
window.rowconfigure(frame, weight=1, minsize=50)


frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )

frame.grid(row=1, column=2)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=2, column=2)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=3, column=2)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()
window.columnconfigure(frame, weight=1, minsize=75)
window.rowconfigure(frame, weight=1, minsize=50)


frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=1, column=3)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=2, column=3)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

frame.grid(row=3, column=3)
label = tk.Label(master=frame, text=f"Row \nColumn ")
label.pack()

window.columnconfigure(frame, weight=1, minsize=75)
window.rowconfigure(frame, weight=1, minsize=50)



window.mainloop()
