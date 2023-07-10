# классы + файлы
from tkinter import *
import os

root = Tk()
root.title("Список")

class Student:
    def __init__(self, fio, age):
        self.fio = fio
        self.age = age
    def __str__(self):
        return f"{self.fio} {self.age}"
    def getFio(self):
        return self.fio
    def setFio(self, ver):
        self.fio = ver
    def getAge(self):
        return self.age
    def setAge(self, var):
        self.age = var
class Table:
    def __init__(self):
        f1 = Frame()
        f2 = Frame()
        f1.pack(side=LEFT)
        f2.pack(side=LEFT)
        self.e1 = Entry(f2, width=20, font=("Ariel", 27))
        self.e2 = Entry(f2, width=20, font=("Ariel", 27))
        b = Button(f2, text="Добавить", width=10, font=("Ariel", 27), command=self.add_man)
        self.e1.pack()
        self.e2.pack()
        b.pack()
        self.mas = []
        self.lbx_man = Listbox(f1, width=20, font=("Ariel", 27))
        dir_students = os.listdir("students")
        for i in dir_students:
            with open(f"students/{i}", "r") as f:
                s=f.read()
                self.lbx_man.insert(END, s)
                self.mas.append(Student(i, s.split()[1]))
                print(s.split())
        self.lbx_man.pack()

    def add_man(self):
        self.mas.append(Student(self.e1.get(), self.e2.get()))
        self.lbx_man.insert(END, f"{self.e1.get()} {self.e2.get()}")
        with open(f"students/{self.e1.get()}", "w") as f:
            f.write(f"{self.e1.get()} {self.e2.get()}")
        self.e1.delete(0, END)
        self.e2.delete(0, END)

a = Table()
root.mainloop()
