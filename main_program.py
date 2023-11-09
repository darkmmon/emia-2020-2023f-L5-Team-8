import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os.path


def validation(target_user, target_pass,DateOfBirth):
    f=open("userdata.txt","r+")
    data=f.readlines()
    for i in range(len(data)):
        data[i]= data[i].split()
    flag = False
    for line in data:
        if line[0] == target_user:
            flag = True
    if flag ==True:
        messagebox.showinfo(title="Message", message="Dulplicate username")
        signup()
    if flag == False:
        data.append([target_user,target_pass,DateOfBirth])
        f.write(target_user+' '+target_pass+' '+DateOfBirth+' '+"\n")
        f.close()
        messagebox.showinfo(title="Message", message="Successfully create account")
        login()

def check_user(target_user,target_pass):
    f=open("userdata.txt","r+")
    data=f.readlines()
    for i in range(len(data)):
        data[i]= data[i].split()
    print(data)
    flag = False
    for line in data:
        if line[0] == target_user and line[1] == target_pass:
            flag = True
    f.close()
    if flag ==True:
        messagebox.showinfo(title="Message", message="login successfully, welcom "+target_user)
        signup()
    if flag == False:
        messagebox.showinfo(title="Message", message="The username dosen't match with the password")
        login()
def signup():
    signup_window = tk.Tk()
    signup_window.geometry("800x500")
    signup_window.title("Sign up")

    title = tk.Label(signup_window, text="Creat your personal account", font= ('Arial' ,18))
    title.pack(padx= 20, pady=20)

    frame = tk.Frame(signup_window)
    frame.columnconfigure(0,weight=2)
    frame.columnconfigure(1,weight=2)
    frame.columnconfigure(2,weight=2)
    frame.columnconfigure(3,weight=2)

    username = tk.Label(frame, text="username:", font= ('Arial' ,18))
    username.grid(row= 0, column=0, sticky=tk.E +tk.W)
    my_user_name = tk.Entry(frame)
    my_user_name.grid(row=0, column=1)

    password = tk.Label(frame, text="password:", font= ('Arial' ,18))
    password.grid(row= 3, column=0, sticky=tk.E +tk.W)
    my_password = tk.Entry(frame)
    my_password.grid(row=3, column=1)

    dayOfBirth = tk.Label(frame, text="Date of Birth:", font= ('Arial' ,18))
    dayOfBirth.grid(row= 5, column=0, sticky=tk.E +tk.W)
    my_dayOfBirth = tk.Entry(frame, text= "YYYYMMDD")
    my_dayOfBirth.grid(row=5, column=1)

    frame.pack()

    button_2 = tk.Button(signup_window, text= "Enter", font= ("Arial", 15), command=lambda :validation(my_user_name.get(),my_password.get(),my_dayOfBirth.get()))
    button_2.pack()
    signup_window.mainloop()



def login():
    main_window = tk.Tk()
    main_window.geometry("800x500")
    main_window.title("Login")

    title = tk.Label(main_window, text="Sign in", font= ('Arial' ,18))
    title.pack(padx= 20, pady=20)

    frame = tk.Frame(main_window)
    frame.columnconfigure(0,weight=2)
    frame.columnconfigure(1,weight=2)
    frame.columnconfigure(2,weight=2)
    frame.columnconfigure(3,weight=2)

    username = tk.Label(frame, text="username:", font= ('Arial' ,18))
    username.grid(row= 0, column=0, sticky=tk.E +tk.W)
    my_user_name = tk.Entry(frame)
    my_user_name.grid(row=0, column=1)

    password = tk.Label(frame, text="password:", font= ('Arial' ,18))
    password.grid(row= 3, column=0, sticky=tk.E +tk.W)
    my_password = tk.Entry(frame)
    my_password.grid(row=3, column=1)

    frame.pack()

    check_state = tk.IntVar()

    button_1 = tk.Checkbutton(main_window, text= "Check", font= ("Arial", 15), variable= check_state )
    button_1.pack()

    button_2 = tk.Button(main_window, text= "Enter", font= ("Arial", 15),command=lambda: check_user(my_user_name.get(),my_password.get()))
    button_2.pack()

    line = tk.Label(main_window, text="_________________________________________________")
    line.pack()

    sign_up_button = tk.Button( main_window, text="Click here to creat an account", font= ("Arial", 15),command=signup)
    sign_up_button.pack()

    main_window.mainloop()




login()