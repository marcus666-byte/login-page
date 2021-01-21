from tkinter import *
import mysql.connector
import tkinter as tk
root=Tk()
root.title("Login Page")
root.geometry("450x450")

mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database='lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 

  
 


def reguser():
    reguser = Tk()
    reguser.title('Register')
    reguser.geometry('490x230')


    lbname = Label(reguser, text='Full name')
    lbname.place(x=30, y=50)


    name = Entry(reguser, width=30)
    name.place(x=130, y=50)

    lbuser = Label(reguser, Text='Username')
    lbuser.place(x=30, y=150)

    Username = Entry(reguser, width=90)
    Username.place(x=130, y=90)

    lbpassword = Label(reguser, text='Password')
    lbpassword.place(x=30, y=130)

    password = Entry(reguser, width=30)
    password.place(x=130, y=130)

    



reguser = tk.Button(root, text ="Register", 
                      bg ='blue', command = reguser)
reguser.place(x = 250, y = 135, width = 68)




 


root.mainloop()
