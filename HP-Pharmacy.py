from customtkinter import *
import tkinter
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk
import time

set_default_color_theme("green")
phar = CTk()
phar.title("Pharmacy Login System")
phar.iconbitmap("istock.ico")
phar.resizable(0,0)
phar.state("zoomed")

my_image1 = CTkImage(light_image=Image.open("Picsart.png"),dark_image=Image.open("Picsart.png"),size=(50, 50))

head = CTkLabel(master=phar, text="Pharmacy Management System",text_color="black",font=("times",34),bg_color="cyan4",height=55,image=my_image1,compound=RIGHT)
head.pack(fill="both")

my_image2 = Image.open("health.png")
resized_image = my_image2.resize((2600,1420))
converted_image = ImageTk.PhotoImage(resized_image)
mylable = tkinter.Label(phar,image=converted_image,width=2700,height=1390)
mylable.pack()

frame1 = CTkFrame(master=mylable, width=350, height=420,corner_radius=11,border_width=2,border_color='white',bg_color='white')
frame1.place(relx=0.17, rely=0.45, anchor=tkinter.CENTER)

l1 = CTkLabel(master=frame1, text="Log into your System" ,font=("century gothic",20))
l1.place(x=73,y=15)


email_box1 = CTkEntry(master=frame1,placeholder_text='Enter your E-Mail',border_width=3,width=250,height=50)
email_box1.place(x=50,y=80)

password_box1 = CTkEntry(master=frame1,placeholder_text='Enter your Password',show='*',border_width=3,width=250,height=50)
password_box1.place(x=50,y=145)

showw = IntVar(value=0)
def show():
    if (showw.get() == 0):  # checkbutton passes value 1 for true and 0 for false
        password_box1.configure(show='*')  # config is used to access widget's attributes after its initialization
    else :
        password_box1.configure(show='')


# show password checkbutton
CTkCheckBox(frame1,text='Show pasword', offvalue=0, variable=showw,border_width=2,border_color='lawngreen',font=('century gothic',9),checkbox_height=15,checkbox_width=15 ,command=show,).place(x=60, y=200)

#creates a database table for login####
try:
    conn = sqlite3.connect('admins.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE users(
        first_name text,
        last_name text,
        email text,
        phone integer,
        ps text,
        psc text,
        ques text
        )""")
    conn.commit()
    conn.close()
except:
    pass



def login():
    a = email_box1.get()
    b = password_box1.get()

    conn = sqlite3.connect('admins.db')
    c = conn.cursor()
    c.execute("SELECT * from users")
    rec = c.fetchall()
    i = len(rec) - 1
    print(rec[i][2],'     ',rec[i][4])

    if rec[i][2] == a and rec[i][4] == b:
        phar.destroy()
        import phar_login

    else:
        messagebox.askretrycancel("Login Failed","Your Username or Password is incorrect.\n\t Please Try Again.")

    conn.commit()
    conn.close()

login_btn = CTkButton(master=frame1, text="Login",font=("times",20),text_color="black",width=250,height=40,fg_color='lawngreen',hover_color="darkgreen",command=login)
login_btn.place(x=50,y=250)

def forget_page():
    edit = CTk()
    edit.title('Forget Password')
    edit.geometry('400x480')
    edit.resizable(0,0)
    edit_head = CTkLabel(master=edit, text="Reset Password", text_color="black", font=("Century Gothic", 21),bg_color="forestgreen")
    edit_head.pack(fill="both")

    email_box2 = CTkEntry(master=edit, placeholder_text="Enter Your E-mail Address", border_width=3, width=250, height=50)
    email_box2.place(x=70, y=100)

    password_box2 = CTkEntry(master=edit, placeholder_text="Enter New Password", border_width=3, width=250, height=50)
    password_box2.place(x=70, y=170)

    securityq_box2 = CTkEntry(master=edit, placeholder_text="What is your childhood school name?", border_width=3, width=250, height=50)
    securityq_box2.place(x=70, y=240)

    def forg():
        conn = sqlite3.connect('admins.db')
        c = conn.cursor()
        c.execute("SELECT * from users")
        rec = c.fetchall()
        i = len(rec) - 1

        if email_box2.get()==rec[i][2] and securityq_box2.get()==rec[i][6]:
            conn = sqlite3.connect('admins.db')
            c = conn.cursor()
            c.execute("""UPDATE users SET ps = :pasc""",{'pasc': password_box2.get()})
            conn.commit()
            conn.close()

            messagebox.showinfo("Reset Password","Your Password has been changed.")
            edit.destroy()

    instruct_btn = CTkButton(master=edit, text="Change Password",font=("times",20),text_color="black",width=250,height=40,fg_color='lawngreen',hover_color="darkgreen",command=forg)
    instruct_btn.place(x=70,y=340)

    edit.mainloop()


def signup():
    edit2 = CTk()
    edit2.title('Sign up')
    edit2.geometry('400x520')
    edit2.resizable(0,0)
    edit_head = CTkLabel(master=edit2, text="Create your Account", text_color="black", font=("Century Gothic", 21),bg_color="royalblue")
    edit_head.pack(fill="both")

    def submit():
        if password_box.get() == confirm_box.get() and len(phone_box.get())>=10:
            conn = sqlite3.connect('admins.db')
            c = conn.cursor()
            c.execute("INSERT INTO users VALUES (:f_name, :l_name,:email, :phone, :ps, :psc,:ques)",
                      {'f_name': f_name_box.get(), 'l_name': l_name_box.get(), 'email': email_box.get(),
                       'phone': phone_box.get(), 'ps': password_box.get(), 'psc': confirm_box.get(),'ques':securityq_box.get()})

            messagebox.showinfo("Sign Up", "Account created Sucessfully")
            conn.commit()
            conn.close()
            edit2.destroy()
        else:
            messagebox.showinfo('Technical Error',"Check Your Informations")

    global f_name_box
    global l_name_box
    global email_box
    global phone_box
    global password_box
    global confirm_box
    global securityq_box

    f_name_box = CTkEntry(master=edit2, placeholder_text="First Name", border_width=3, width=120, height=40)
    f_name_box.place(x=70, y=80)

    l_name_box = CTkEntry(master=edit2, placeholder_text="Last Name", border_width=3, width=120, height=40)
    l_name_box.place(x=210, y=80)

    email_box = CTkEntry(master=edit2, placeholder_text="E-Mail", border_width=3, width=260, height=40)
    email_box.place(x=70, y=140)

    phone_box = CTkEntry(master=edit2, placeholder_text="Phone Number", border_width=3, width=260, height=40)
    phone_box.place(x=70, y=200)

    password_box = CTkEntry(master=edit2, placeholder_text="Password", border_width=3, width=120, height=40)
    password_box.place(x=70, y=260)

    confirm_box = CTkEntry(master=edit2, placeholder_text="Confirm", border_width=3, width=120, height=40)
    confirm_box.place(x=210, y=260)

    securityq = CTkLabel(edit2,text="Security Question :", text_color="black", font=("Century Gothic", 15))
    securityq.place(x=70,y=340)
    securityq_box = CTkEntry(master=edit2, placeholder_text="What is your childhood school name?", border_width=3, width=260, height=30)
    securityq_box.place(x=70, y=370)


    submit_btn = CTkButton(master=edit2, text="Sign Up",font=("times",20),text_color="black",width=260,height=35,fg_color='royalblue',hover_color="darkgreen",command=submit)
    submit_btn.place(x=70,y=440)

    # CTkLabel(edit,font=("Century Gothic",10),text='   By clicking Sign Up, you agree to our Terms, Privacy Policy and Cookies Policy.\nYou may receive SMS Notifications from us and can opt out any time.').place(y=430)

    edit2.mainloop()


forget_btn = CTkButton(master=frame1,text="Forget Password?",text_color=('black','white'),font=("Century Gothic",15),fg_color="transparent",command=forget_page)
forget_btn.place(x=110,y=295)

signup_label = CTkLabel(master=frame1, text="Don't have an account?", font=("century gothic",15),text_color='grey')
signup_label.place(x=30,y=370)

signup_btn = CTkButton(master=frame1,text="Sign Up",text_color=('black','white'),font=("Century Gothic",17),fg_color="transparent",width=100,height=35,border_color='lawngreen',border_width=2,hover_color="royalblue",command=signup)
signup_btn.place(x=230,y=365)

switch_var = StringVar(value="light")
def switch_event():
    set_appearance_mode(switch_var.get())

dark_switch = CTkSwitch(phar, text="Dark mode",font=("Century Gothic",15),button_color='lightgrey',progress_color='dimgrey', command=switch_event,variable=switch_var, onvalue="dark", offvalue="light")
dark_switch.pack(anchor='s',side='left',padx=15)


tail1 = CTkLabel(phar, text=(time.asctime()),text_color=('black',"white"),font=("century gothic",11))
tail1.pack(side=RIGHT,anchor='n',padx=10)

phar.mainloop()