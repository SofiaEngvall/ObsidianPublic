import tkinter as tk

win = tk.Tk()

win.geometry("500x500")
win.title("Update OBS Paths")

label = tk.Label(win, text="hi",  font=('Arial', 18))
label.pack(padx=10, pady=10)

entry = tk.Entry(win, font=('Arial', 18))
entry.pack(padx=10, pady=10)

textbox = tk.Text(win, height=5, font=('Arial', 18))
textbox.pack(padx=10, pady=10)

button = tk.Button(win, text="hi", font=('Arial', 18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(win)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

button2 = tk.Button(win, text="there", font=('Arial', 18))
button2.place(x=200, y=200, height=50, width=50)

win.mainloop()
