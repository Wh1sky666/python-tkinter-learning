import tkinter as tk
from random import choice
from tkinter import messagebox


def addLesson():
    value = EnterText.get()
    if value != '':
        with open('001.txt', 'a+', encoding="utf-8") as file:
            file.write(value + '\n')
        EnterText.delete(0, 'end')
    else:
        tk.messagebox.showinfo("Ошибка", 'Поле для ввода пустое')


def randomIdea():
    with open('001.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo("Идея", (choice(lines)))


def EnterClick(q):
    addLesson()


window = tk.Tk()

window.resizable(width=False, height=False)

window.title('Генератор уроков')

window.geometry('720x360')

window["bg"] = "black"

name = tk.Label(window, text="Добавить урок", font=("Times new roman", 20), fg="white", bg="black")
name.place(x=20, y=25)

EnterText = tk.Entry(fg="black", width=47)
EnterText.place(x=50, y=80)

buttom = tk.Button(window, text="Добавить!", command=addLesson, width="20", height="1", fg="black", bg="white")
buttom.place(x=350, y=80)

window.bind('<Return>', EnterClick)

generate = tk.Label(window, text="Сгенерировать урок", font=("Times new roman", 20), fg="white", bg="black")
generate.place(x=20, y=150)

buttom_generate = tk.Button(window, text="Сгенерировать", command=randomIdea, width="20", height="1", fg="black",
                            bg="white")
buttom_generate.place(x=350, y=160)

window.mainloop()
