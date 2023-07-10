from tkinter import *

root = Tk()

f1 = Frame()
f2 = Frame()
f3 = Frame()
f4 = LabelFrame()
b1 = Button(f1, text="Добавить студента: ", font=15)
b2 = Button(f2, text="Добавить оценку", font=10)
e1 = Entry(f1, relief=SOLID, font=5)
l2 = Label(f4, width=40, font=15)
l3 = Label(f4, width=40, font=15)
l4 = Label(f4, width=40, font=15)
b3 = Button(f4, text="Добавить оценку: ", width=20, font=15)
b4 = Button(f4, text="Закрыть", font="Arial 10")
e2 = Entry(f4, width=20, font=15)
lbx1 = Listbox(f1, height=10, width=20, font="Arial 15", selectmode=EXTENDED)
student_obj = list()
class Student:
    def __init__(self, fio):
        self.fio = fio
        self.marks = list()
    def getFio(self):
        return self.fio
    def setFio(self, fio):
        self.fio = fio

    def getMarks(self):
        return self.marks

    def setMarks(self, marks):
        self.marks = marks

    def Add_mark(self, mark):
        self.marks.append(mark)

    def __str__(self):
        return f"{self.fio} {', '.join(self.marks)}"

def b1Funk(event):
    student_obj.append(Student(e1.get()))
    lbx1.insert(END, e1.get())
    e1.delete(0, END)

def b2Funk(event):
    for i in student_obj:
        if i.getFio() == lbx1.get(lbx1.curselection()):
            f4.pack(side=LEFT, fill=Y)
            l2['text'] = f"Имя: \n{i.getFio()}"
            l3['text'] = f"Оценки: \n{' '.join(i.getMarks())}"
            b3.pack()
            e2.pack()

def b3Funk(event):
    for i in student_obj:
        if i.getFio() == lbx1.get(lbx1.curselection()):
            i.Add_mark(e2.get() + ",")
            e2.delete(0, END)
            i.Add_mark(e2.get())
            l3['text'] = f"Оценки: \n{' '.join(i.getMarks())}"
def b4Funk(event):
    f4.pack_forget()
    l2['text'] = ' '
    l3['text'] = ' '

f1.pack(side=LEFT)
f2.pack(side=LEFT)
f3.pack(side=LEFT)
e1.pack()
b1.bind("<Button-1>", b1Funk)
b1.pack()
b2.bind("<Button-1>", b2Funk)
b2.pack()
lbx1.pack()
b4.pack(anchor=NE)
l2.pack()
l3.pack()
b4.bind("<Button-1>", b4Funk)
b3.bind("<Button-1>", b3Funk)
l4.pack()
b2.pack()


root.mainloop()