import tkinter as tk

window = tk.Tk()
window.title("Car Loan Calculator")
window.geometry("800x500")

my_label = tk.Label(
    window,
    text="Hello world",
    fg="white",
    bg="black",
    font=("Times New Roman", 32),
)
my_label.grid(row=0, column=0)

my_label2 = tk.Label(window, text="Second thing")
my_label2.grid(row=1, column=1)

window.mainloop()
