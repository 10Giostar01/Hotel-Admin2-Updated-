import tkinter
from tkinter import Toplevel
import json
import database
from database import Database

window = tkinter.Tk()

window.title("Giostar Hotels (Administration)")
window.geometry("500x500")

window.mainloop()


class GUI:
    def __init__(self):
        self.customers = None
        self.database = Database()
        self.positions = []
        self.pull()
        self.generateLayout()


    def pull(self):
         self.database.pull()
         with open('firebase_data.json', 'r') as f:
            file_contents = json.load(f)
            self.customers = (list(file_contents.keys()))

    def generateLayout(self):
          for i in range(len(self.customers)):
            self.button = tkinter.Button(window, text=self.customers[i], font=("Arial", 15), width=15, command=self.openInformation)
            self.button.grid(row=0, column=i, sticky=tkinter.W + tkinter.E)
            self.positions.append(self.customers[i])

    def openInformation(self):
            new_window = Toplevel(window)
            new_window.title('Customer Info')
            new_window.geometry("500x500")

            for i in range(len(self.positions)):

                Name = tkinter.Label(new_window, text= self.positions[i] , font = ('Airial', 18))
                Name.grid(row = 1, column = 0, sticky = tkinter.W + tkinter.E)

                Card = tkinter.Label(new_window, text= self.positions[i], font = ('Airial', 18))
                Card.grid(row = 2, column = 0, sticky = tkinter.W + tkinter.E)

                Phone = tkinter.Label(new_window, text= self.positions[i], font = ('Airial', 18))
                Phone.grid(row = 3, column = 0, sticky = tkinter.W + tkinter.E)

                Stay = tkinter.Label(new_window, text= self.positions[i], font = ('Airial', 18))
                Stay.grid(row = 4, column = 0, sticky = tkinter.W + tkinter.E)

    






gui = GUI()

