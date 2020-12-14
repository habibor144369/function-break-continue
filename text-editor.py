from tkinter import *
User_graphics = Tk()
User_graphics.geometry('500x400')

User_graphics.title("Hello Developer")

def button_command():
    text = entry.get()
    print(text)
    return None

def text_clear():
    entry.delete(0, END)
    return None

t = ("poppins", 20, "bold")
b = ("poppins", 12)

entry = Entry(User_graphics, width = 30, font = t, justify='center')
entry.pack()

Button(User_graphics, text = 'Click Button', font = b, command = button_command).pack()
Button(User_graphics, text = 'Clear Text', font = b, command = text_clear).pack()

User_graphics.mainloop()
print('program terminated!')
