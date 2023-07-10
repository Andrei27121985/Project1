from getpass import getpass

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "postgresql://postgres:2712198527121985@localhost/BH1"
#в SQL и из
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from tkinter import *
engine = create_engine(sqlite_database, echo=True)

class Wind:
    def __init__(self):
        f = Frame()
        f.pack(side=LEFT)
        Label(f, text="Имя и сумма", font=("Ariel", 27)).pack()
        self.e = Entry(f, width=10, font=("Ariel", 27))
        self.e.bind("<Return>", self.inText)
        self.t = Text(f, width=20, height=10, font=("Ariel", 27))
        self.load()
        self.e.pack()
        self.t.pack()
        # Button(f, text="сохранить", width=10, font=("Ariel", 27), command=self.save).pack()

    def getEntry(self):
        return self.e.get()
    def delEntry(self):
        self.e.delete(0, END)
    def inText(self, event):
        self.t.insert(END, self.getEntry())
        name = self.getEntry().split()[0]
        money = self.getEntry().split()[1]
        with Session(autoflush=False, bind=engine) as db:
            obj = Customer(name=name, money=money)
            db.add(obj)
            db.commit()
        self.delEntry()

    def load(self):
        with Session(autoflush=False, bind=engine) as db:
            cus = db.query(Customer).all()
            out_txt = ""
            for i in cus:
                out_txt += str(i) + "\n"
        self.t.insert(END, out_txt)

class Base(DeclarativeBase):
    pass
class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    money = Column(Integer)
    def __repr__(self):
        return f"{self.name} {self.money}"
        # return f"{self.id} {self.name} {self.money}"


root = Tk()
root.title("window")
news = Wind()
root.mainloop()
