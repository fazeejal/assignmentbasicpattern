##calculator

# import tkinter as tk

# def on_button_click(value):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + value)

# def on_clear():
#     entry.delete(0, tk.END)

# def on_equal():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create the main window
# root = tk.Tk()
# root.title("Simple Calculator")

# # Entry widget for display
# entry = tk.Entry(root, width=16, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
# entry.grid(row=0, column=0, columnspan=4)

# # Buttons
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]

# row_val = 1
# col_val = 0

# for button in buttons:
#     tk.Button(root, text=button, width=4, height=2, command=lambda b=button: on_button_click(b) if b != '=' else on_equal()).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# # Clear button
# tk.Button(root, text="C", width=4, height=2, command=on_clear).grid(row=row_val, column=col_val)

# # Run the main loop
# root.mainloop()

##2

# from tkinter import *
# root=Tk()
# root.title("assignment")
# root.geometry('500x500')
# def printentry():
#     w=e1.get()
#     result_label = Label(root, text="Entered Name: " + w)
#     result_label.pack()
   
# l1=Label(root,text="name")
# l1.pack()
# e1=Entry(root)
# e1.pack()
# b1=Button(root,text="click",command=printentry)
# b1.pack()
# root.mainloop()

##3
from tkinter import *
root= Tk()
root.title("assignment")
l1=Label(root,text="hellow world",bg="red",font=("times",18))
l1.pack()
root.mainloop()