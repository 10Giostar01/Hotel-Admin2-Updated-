import tkinter
from tkinter import Toplevel
from tkinter import Label





class Gui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Giostar Hotels')
        self.window.geometry('500x500')
        self.buttons = []

    def FinalizeInitialize(self):

        for i in range(len(self.buttons)):
            self.buttons[i].grid(row = 0, column = i, sticky = tkinter.W + tkinter.E)
        self.window.mainloop()
   
    def open_new_window(self, customer):
        print(customer)
        new_window = tkinter.Toplevel(self.window)
        new_window.title(customer["name"])
        new_window.geometry("300x200")

# itterate over customer information and pack as lables
        row = 0
        for key,value in customer.items():
            column =0
            discription = Label(new_window, text = key+" :")
            information = Label(new_window, text = value)
            discription.grid(row = row, column = 0, padx = 2)
            information.grid(row = row, column = 1, padx = 2)
            row += 1
            
    
        close_button = tkinter.Button(new_window, text="Close", command=new_window.destroy)
        close_button.grid(row = 5, column = 1)

class CustomerGui(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.customers = [ 
            {"name" : "customer1", "credit": "credit1" , "phone": "phone1", "stay": "stay1"},
            {"name" : "customer2", "credit": "credit2" , "phone": "phone2", "stay": "stay2"},
            {"name" : "customer3", "credit": "credit3" , "phone": "phone3", "stay": "stay3"},
            ]

        for i in range(len(self.customers)):
            button = tkinter.Button(self.window, text=self.customers[i]["name"], font=("Arial", 15), width = 15, textvariable = str(i), command =lambda: self.open_new_window(self.customers[i]))
            self.buttons.append(button)

        print(self.buttons[0].configure())
            


"""
l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")
 
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
"""


"""

    let customer = setState(undefined)
    let customer_number = 0

    for each button:
        onClick = open_customer(customer_number)
        customer_number +=1

    """

gui = CustomerGui()
gui.FinalizeInitialize()

