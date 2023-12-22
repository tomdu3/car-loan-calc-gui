import tkinter as tk

window = tk.Tk()
window.title("Car Loan Calculator")
window.geometry("800x500")

my_label = tk.Label(window, text='Hello world', fg='white', bg='black', font=('Helvetica', 32), width=100)
my_label.pack()

my_label2 = tk.Label(window, text='Second thing')
my_label2.pack(pady=20)

window.mainloop()



