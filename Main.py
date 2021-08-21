# ***********************

# ATM project for compiler material under the supervision of Dr.Hatem

# ***********************
# BY :
# Mohamed Faryed
# Mahoud Turky
# Mohamed Ali
# Osamaa El-Mekawe
# ***********************

from tkinter import *
from tkinter import messagebox
import sqlite3

trial = 0
ARIAL = ("arial", 10, "bold")

class Bank:
    def __init__(self, root):
        trial = 0
        self.conn = sqlite3.connect("atm_databse.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(self.root,text="ATM",bg="#b8c52b",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root,bg="#038b59",width=600,height=430)
        #Login Page Form Components
        self.userlabel =Label(self.frame,text="Account Number",bg="#038b59",fg="white",font=ARIAL)
        self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#b8c52b",
           highlightthickness=2,
            highlightbackground="white")
        self.plabel = Label(self.frame, text="Password",bg="#038b59",fg="white",font=ARIAL)
        self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#b8c52b",
           highlightthickness=2,
            highlightbackground="white")
        self.button = Button(self.frame,text="LOGIN",bg="#b8c52b",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Quit",bg="#b8c52b",fg="white",font=ARIAL,command = self.root.destroy)
        self.userlabel.place(x=145,y=100,width=120,height=20)
        self.uentry.place(x=153,y=130,width=200,height=20)
        self.plabel.place(x=125,y=160,width=120,height=20)
        self.pentry.place(x=153,y=190,width=200,height=20)
        self.button.place(x=155,y=230,width=120,height=20)
        self.q.place(x=480,y=360,width=120,height=20)


        self.frame.pack()
    def database_fetch(self):#Fetching Account data from database
        self.acc_list = []
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ",(self.ac,))
        for i in self.temp:
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.acc_list.append("Account type = {}".format(i[3]))
            self.ac = i[2]
            self.mony = i[4]
            self.acc_list.append("Balance = {}".format(i[4]))

    def verify(self):#verifying of authorised user
        ac = False
        mony = False
        global trial
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ", (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                trial += 1
                left_tries = 3 - trial
                if trial >= 3:
                    m = " Login UnSucessFull! Your card is withdrawn. Go to bank to get it. "
                    messagebox._show("Login Info!", m)
                else:
                    m = " Login UnSucessFull ! Wrong Password You have " + str(left_tries) + " tries!!!"
                    messagebox._show("Login Info!", m)

        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)


    def MainMenu(self):#Main App Appears after logined !
        self.frame = Frame(self.root,bg="#038b59",width=800,height=400)
        root.geometry("800x430")
        self.detail = Button(self.frame,text="Account Details",bg="#b8c52b",fg="white",font=ARIAL,command=self.account_detail)
        self.enquiry = Button(self.frame, text="Balance Enquiry",bg="#b8c52b",fg="white",font=ARIAL,command= self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money",bg="#b8c52b",fg="white",font=ARIAL,command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money",bg="#b8c52b",fg="white",font=ARIAL,command=self.withdrawl_money)
        self.chpass = Button(self.frame, text="Change Password",bg="#b8c52b",fg="white",font=ARIAL,command=self.change_pin)
        self.q = Button(self.frame, text="Quit", bg="#b8c52b", fg="white", font=ARIAL, command=self.root.destroy)
        self.detail.place(x=0,y=0,width=200,height=50)
        self.enquiry.place(x=0, y=315, width=200, height=50)
        self.deposit.place(x=600, y=0, width=200, height=50)
        self.withdrawl.place(x=600, y=315, width=200, height=50)
        self.chpass.place(x=600, y=150, width=200, height=50)
        self.q.place(x=340, y=340, width=120, height=20)
        self.frame.pack()

    def account_detail(self):
        self.database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[1]+"\n"+self.acc_list[2]
        self.label = Label(self.frame, text=text, font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text=self.acc_list[3],font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)

    def deposit_money(self):
        self.label = Label(self.frame, text="Enter the deposit value", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#b8c52b",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit",bg="#b8c52b", fg="white", font=ARIAL)

        self.money_box.place(x=200, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.deposit_trans)

    def deposit_trans(self, flag):
        if self.money_box.get() == str(self.money_box.get()):
           self.label = Label(self.frame, text="ERROR", font=ARIAL)
           self.label.place(x=200, y=100, width=300, height=100)

        if float(self.money_box.get()) < 0:
             self.label = Label(self.frame, text="No value", font=ARIAL)
             self.label.place(x=200, y=100, width=300, height=100)

        else:
             self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
             self.label.place(x=200, y=100, width=300, height=100)
             self.conn.execute("update atm set bal = bal + ? where acc_no = ?", (self.money_box.get(),self.ac))
             self.conn.commit()

    def withdrawl_money(self):
        self.label = Label(self.frame, text="Enter the withdraw value", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#b8c52b",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#b8c52b",fg="white",font=ARIAL)

        self.money_box.place(x=200,y=100,width=200,height=20)
        self.submitButton.place(x=445,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self, flag):
        self.database_fetch()
        if self.money_box.get() == str(self.money_box.get()):
           self.label = Label(self.frame, text="ERROR", font=ARIAL)
           self.label.place(x=200, y=100, width=300, height=100)

        if float(self.money_box.get()) > float(self.mony):
            self.label = Label(self.frame, text="There is not enough money", font=ARIAL)
            self.label.place(x=200, y=100, width=300, height=100)

        elif float(self.money_box.get()) < float(self.mony):
          self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
          self.label.place(x=200, y=100, width=300, height=100)
          self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
          self.conn.commit()
    def change_pin(self):
        self.label = Label(self.frame, text="Enter the new pin", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.pin_box = Entry(self.frame, bg="honeydew", highlightcolor="#b8c52b", highlightthickness=2, highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#b8c52b", fg="white", font=ARIAL)
        self.pin_box.place(x=200, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.change_pin_fun)

    def change_pin_fun(self, flag):
        if self.pin_box.get() == str(self.pin_box.get()):
           self.label = Label(self.frame, text="Enter a number!!!", font=ARIAL)
           self.label.place(x=200, y=100, width=300, height=100)

        if float(self.pin_box.get()) < 1000:
             self.label = Label(self.frame, text="Wrong Value, Try again!!!", font=ARIAL)
             self.label.place(x=200, y=100, width=300, height=100)

        else:
             self.label = Label(self.frame, text="Your pin has changed.", font=ARIAL)
             self.label.place(x=200, y=100, width=300, height=100)
             self.conn.execute("update atm set pass = ? where acc_no = ?", (self.pin_box.get(), self.ac))
             self.conn.commit()




root = Tk()
root.title("LOG IN ")
root.geometry("600x430")
icon = PhotoImage(file="ll.png")
root.tk.call("wm", 'iconphoto', root._w, icon)
obj = Bank(root)
root.mainloop()
