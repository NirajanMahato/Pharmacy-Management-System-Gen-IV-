from customtkinter import *
import tkinter
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk
import time

loginP = CTk()
loginP.title("patient registration page")
loginP.resizable(0, 0)
loginP.state('zoomed')
loginP.iconbitmap("istock.ico")
set_default_color_theme('green')

#####creating databaseTable for patient records
try:
    conn = sqlite3.connect('admins2.db')            #Creates table
    c = conn.cursor()                   #Query lai excute garxa
    c.execute("""CREATE TABLE patient_records(
        first_name text,
        last_name text,
        patient_id integer,
        address text,
        contact integer
        )""")
    conn.commit()
    conn.close()
except:
    pass

def save():
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("INSERT INTO patient_records VALUES (:f_name, :l_name,:address, :contact,:patient_id)",{'f_name':f_name_box.get(),'l_name':l_name_box.get(),'address':address_box.get(),'contact':cont_box.get(),'patient_id':patient_id_box.get()})

    messagebox.showinfo("Patient Details","Saved Sucessfully")
    conn.commit()
    conn.close()

    f_name_box.delete(0, END)
    l_name_box.delete(0, END)
    patient_id_box.delete(0, END)
    address_box.delete(0, END)
    dob_box.delete(0, END)
    cont_box.delete(0,END)
    sex_combobox.set("")

    ########to display from database
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM patient_records")
    rec = c.fetchall()
    # print(records)

    i = len(rec) - 1
    name_label = CTkLabel(frame3,text=str(rec[i][0])+' '+str(rec[i][1]), font=("century gothic bold",15),text_color='royalblue')
    name_label.place(x=270,y=90)
    address_label = CTkLabel(frame3,text = str(rec[i][2])+'\n'+str(rec[i][3])+'\n'+"Record ID. : "+str(rec[i][5])  , font=("century gothic",12),text_color='royalblue')
    address_label.place(x=270,y=112)
    conn.commit()
    conn.close()


######### Creating database for medicine records  ########
try:
    conn = sqlite3.connect('admins2.db')            #Creates table
    c = conn.cursor()                   #Query lai excute garxa
    c.execute("""CREATE TABLE medicine_records(
        medicine_name text,
        quantity integer,
        rate integer,
        total integer)""")
    conn.commit()
    conn.close()
except:
    pass


def add():
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("INSERT INTO medicine_records VALUES (:med_name, :quant, :rate,:total)",{'med_name':med_name_box.get(),'quant':quantity_box.get(),'rate':rate_name_box.get(),'total':int(quantity_box.get())*int(rate_name_box.get())})
    # messagebox.showinfo("Medicine Details","Added Sucessfully")
    conn.commit()
    conn.close()

    med_type_box.set('')
    rate_name_box.delete(0,END)
    quantity_box.delete(0, END)
    med_name_box.delete(0, END)
    exp_date_box.delete(0, END)
    issued_date_box.delete(0, END)
    dose_box.delete(0, END)

    def tbl():
        table = CTkFrame(loginP, height=580, width=1200, bg_color='white')
        table.place(x=815, y=280)

        try:
            # Try fetching datas from database
            conn = sqlite3.connect('admins2.db')
            c = conn.cursor()
            c.execute("SELECT oid, medicine_name, quantity, rate,total from medicine_records")
            lst = c.fetchall()
            conn.commit()
            conn.close()
        except:
            # Empty list if list doesn't Exist
            lst = []
        finally:
            # Table headings
            lst.insert(0, ('ID', 'Medicine Name', 'Quantity', 'Rate', 'Total'))

        # creating a Table
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            if i == 0:
                # table headings
                fontt = ('Century Gothic', 15, 'bold')
                jus = CENTER
                bgc = 'white'
            else:
                # table datas
                fontt = ('Century Gothic', 13)
                jus = LEFT
                bgc = 'yellow'
            for j in range(total_columns):
                # width for all columns
                if j == 0:
                    wid = 40
                elif j == 1:
                    wid = 150
                elif j == 2:
                    wid = 100
                elif j == 3:
                    wid = 70
                elif j == 4:
                    wid = 80
                else:
                    wid = 8
                e = CTkEntry(table, width=wid, font=fontt, justify=jus)
                e.grid(row=i, column=j)
                e.insert(0, lst[i][j])
                e.configure(state=DISABLED)

    ####calling table function
    tbl()


login_head = CTkLabel(loginP, text="Patient Registration Form", text_color="black", font=("times", 34),bg_color="cyan4",width=50,  height=50)
login_head.pack(fill="both")


my_image2 = Image.open("health2.png")
resized_image = my_image2.resize((2600, 1420))
converted_image = ImageTk.PhotoImage(resized_image)
mylable3 = tkinter.Label(loginP, image=converted_image, width=2700, height=1390)
mylable3.pack()

frame2 = CTkFrame(master=loginP ,width=760, height=200, corner_radius=11, border_width=3, border_color='cyan4',bg_color='paleturquoise')
frame2.place(relx=0.31, rely=0.25, anchor=tkinter.CENTER)

name = CTkLabel(frame2, text="  Patient Name  :", font=("century gothic", 15))
name.place(x=5, y=20)

f_name_box = CTkEntry(frame2, border_width=2, placeholder_text='First Name', width=100, height=21)
f_name_box.place(x=145, y=25)

l_name_box = CTkEntry(frame2, border_width=2, placeholder_text="Last Name", width=100, height=21)
l_name_box.place(x=255, y=25)

patient_id = CTkLabel(frame2,text="Patient ID  :",font=("century gothic", 15))
patient_id.place(x=408,y=20)

patient_id_box = CTkEntry(frame2,border_width=2,placeholder_text='Enter ID of patient',width=213,height=21)
patient_id_box.place(x=522,y=23)

address = CTkLabel(frame2,text="  Address : ",font=("century gothic", 15))
address.place(x=5,y=60)

address_box = CTkEntry(frame2,border_width=2,placeholder_text="Enter the address",width=210,height=21)
address_box.place(x=145,y=65)

dob = CTkLabel(frame2, text="Date of Birth :", font=("century gothic", 15))
dob.place(x=408, y=60)

dob_box = CTkEntry(frame2, border_width=2, placeholder_text='Enter the date of birth', width=213, height=21)
dob_box.place(x=522, y=65)

sex_label = CTkLabel(frame2, text="  Sex :", font=("century gothic", 15))
sex_label.place(x=5, y=140)

def optionmenu_callback(choice):
    sex_box = choice
sex_combobox = CTkOptionMenu(frame2,values=["Male", 'Female'],command=optionmenu_callback,bg_color='transparent',height=21,width=213)
sex_combobox.place(x=145,y=145)
sex_combobox.set("")  # set initial value

cont = CTkLabel(frame2, text="  Contact No.  :", font=("century gothic", 15))
cont.place(x=5, y=100)

cont_box = CTkEntry(frame2, border_width=2, placeholder_text='Enter the Contact No.', width=213, height=21)
cont_box.place(x=145, y=105)

save_btn = CTkButton(frame2,text='Save',fg_color='teal',font=('century gothic bold',20),text_color='black',height=35,width=325,command=save)
save_btn.place(x=410,y=140)

frame4 = CTkFrame(master=loginP, width=760, height=250, corner_radius=11, border_width=3, border_color='cyan4',bg_color='paleturquoise')
frame4.place(relx=0.31, rely=0.6, anchor=tkinter.CENTER)

med_type = CTkLabel(frame4, text="  Medicine Type :", font=("century gothic", 15))
med_type.place(x=5, y=20)

def optionmenu_callback(choice2):
    med_type_box = choice2
med_type_box = CTkOptionMenu(frame4,values=["Liquid", 'Tablets','Semi-Solid'],command=optionmenu_callback,height=21,width=213)
med_type_box.place(x=145,y=25)
med_type_box.set("")

med_name = CTkLabel(frame4, text="  Medicine Name :", font=("century gothic", 15))
med_name.place(x=5, y=60)

med_name_box = CTkEntry(frame4, border_width=2, placeholder_text='Enter the name of Medicine', width=213, height=21)
med_name_box.place(x=145, y=65)

rate_name = CTkLabel(frame4, text="  Rate :", font=("century gothic", 15))
rate_name.place(x=5, y=100)

rate_name_box = CTkEntry(frame4, border_width=2, placeholder_text='Enter the Rate', width=213, height=21)
rate_name_box.place(x=145, y=105)

quantity = CTkLabel(frame4, text="  Quantity :", font=("century gothic", 15))
quantity.place(x=5, y=140)

quantity_box = CTkEntry(frame4, border_width=2, placeholder_text='Enter the Quantity', width=213, height=21)
quantity_box.place(x=145, y=145)

dose = CTkLabel(frame4, text="  Dosage :", font=("century gothic", 15))
dose.place(x=5, y=180)

dose_box = CTkEntry(frame4, border_width=2, placeholder_text='Enter the Dosage', width=213, height=21)
dose_box.place(x=145, y=185)

issued_date = CTkLabel(frame4, text=" Issued Date :", font=("century gothic", 15))
issued_date.place(x=408, y=20)

issued_date_box = CTkEntry(frame4, border_width=2, placeholder_text='Issued Date', width=213, height=21)
issued_date_box.place(x=522, y=25)

exp_date = CTkLabel(frame4, text="  Expiry Date :", font=("century gothic", 15))
exp_date.place(x=405, y=60)

exp_date_box = CTkEntry(frame4, border_width=2, placeholder_text='Expiry Date', width=213, height=21)
exp_date_box.place(x=522, y=65)

add_btn = CTkButton(frame4,text='Add',fg_color='teal',font=('century gothic bold',20),text_color='black',height=35,width=325,command=add)
add_btn.place(x=410,y=175)

##########FRAME3########
frame3 = CTkFrame(master=loginP, width=460, height=500, corner_radius=11, border_width=3, border_color='cyan4',bg_color='paleturquoise')
frame3.place(relx=0.81, rely=0.44, anchor=tkinter.CENTER)


pharmacy_head1 = CTkLabel(master=frame3, text="Pharmacy", text_color="royalblue", font=("century gothic bold", 13))
pharmacy_head1.place(x=10,y=60)

pharmacy_head2 = CTkLabel(master=frame3, text="Name and Details", text_color="royalblue", font=("century gothic bold", 13))
pharmacy_head2.place(x=270,y=60)

date_head3 = CTkLabel(master=frame3, text="Date & Time", text_color="royalblue", font=("century gothic bold", 13))
date_head3.place(x=10,y=5)

date_head4 = CTkLabel(frame3,text=(time.asctime()),text_color=('royalblue'),font=("century gothic",11))
date_head4.place(x=10,y=25)

pharmacy_name = CTkLabel(master=frame3, text="My Local Pharmacy", text_color="royalblue", font=("century gothic bold", 15))
pharmacy_name.place(x=15,y=90)

pharmacy_details = CTkLabel(master=frame3, text="      345 Main Street,\n     Maitidevi,\n    Kathmandu", text_color="royalblue", font=("century gothic",12))
pharmacy_details.place(x=15,y=112)



def delete():
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("DELETE from medicine_records WHERE oid = " + empty_id_box.get())
    messagebox.showinfo("DELETE RECORDS","Deleted Sucessfully")
    conn.commit()
    conn.close()
    empty_id_box.delete(0,END)

def closetab():
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("DELETE FROM medicine_records")
    conn.commit()
    conn.close()
    loginP.destroy()

def update():
    record_id = empty_id_box.get()
    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("""UPDATE medicine_records SET 
    medicine_name = :medi,
    quantity= :quant,
    rate = :rat,
    total = :tot
    WHERE oid = :oid""",
    {
    'medi':med_name_editor.get(),
    'quant': quantity_editor.get(),
    'rat':rate_editor.get(),
    'tot': int(quantity_editor.get())*int(rate_editor.get()),
    'oid':record_id
        }
    )

    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor = CTk()
    editor.title('Update Data')
    editor.geometry('300x400')

    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    record_id = empty_id_box.get()
    c.execute("SELECT * FROM medicine_records WHERE oid="+record_id)
    records = c.fetchall()

    global med_name_editor
    global quantity_editor
    global rate_editor
    # global total_editor

    med_name_label = CTkLabel(editor, text="Medicine Name :", font=("century gothic", 15))
    med_name_label.grid(row=0, column=0, pady=(10, 0))

    quantity_label = CTkLabel(editor, text="Quantity :", font=("century gothic", 15))
    quantity_label.grid(row=1, column=0)

    rate_label = CTkLabel(editor,text="Rate :", font=("century gothi", 15))
    rate_label.grid(row=2, column=0)

    total_label = CTkLabel(editor, text="Total :", font=("century gothic", 15))
    total_label.grid(row=3, column=0)

    med_name_editor = CTkEntry(editor, width=100)
    med_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    quantity_editor= CTkEntry(editor, width=100)
    quantity_editor.grid(row=1,column=1)

    rate_editor = CTkEntry(editor, width=100)
    rate_editor.grid(row=2, column=1)

    total_editor = CTkEntry(editor, width=100)
    total_editor.grid(row=3, column=1)


    for record in records:
        med_name_editor.insert(0, record[0])
        quantity_editor.insert(0, record[1])
        rate_editor.insert(0, record[2])
        total_editor.insert(0, record[3])

    edit_btn = CTkButton(editor, text='UPDATE', command=update,height=40, font=("century gothic bold", 17),text_color='black')
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

    conn.commit()
    conn.close()
    empty_id_box.delete(0, END)

    editor.mainloop()


##########FRAME5  ########
frame5 = CTkFrame(master=loginP, width=1250, height=100, corner_radius=11, border_width=3, border_color='cyan4',bg_color='paleturquoise')
frame5.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)

delete_btn = CTkButton(frame5,text='DELETE',fg_color='teal',font=('century goyhic',20),text_color='black',height=50,width=315,command=delete)
delete_btn.place(x=25,y=26)

empty_id_box = CTkEntry(frame5,border_width=3,border_color='teal',placeholder_text='     Enter ID',width=90,height=50)
empty_id_box.place(x=345,y=26)

update_btn = CTkButton(frame5,text='UPDATE',fg_color='teal',font=('century goyhic',20),text_color='black',height=50,width=310,command=edit)
update_btn.place(x=440,y=26)

def query():
    P = CTk()
    P.title("Medicine Records")
    P.geometry('470x400')
    set_default_color_theme('green')


    med_name_label = CTkLabel(P, text="Medicine Name", font=("century gothic bold", 15), text_color='royalblue')
    med_name_label.place(x=20, y=4)

    quantity_label = CTkLabel(P, text="Quantity", font=("century gothic bold", 15), text_color='royalblue')
    quantity_label.place(x=155, y=4)

    rate_label = CTkLabel(P, text="Rate", font=("century gothic bold", 15), text_color='royalblue')
    rate_label.place(x=240, y=4)

    total_label = CTkLabel(P, text="Total", font=("century gothic bold", 15), text_color='royalblue')
    total_label.place(x=305, y=4)

    id_label = CTkLabel(P, text="ID", font=("century gothic bold", 15), text_color='royalblue')
    id_label.place(x=380, y=4)

    conn = sqlite3.connect('admins2.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM medicine_records")
    records = c.fetchall()

    print_record=''
    for record in records:
        print_record += str(record[0])+'\t\t'+str(record[1])+ '\t' +str(record[2])+ '  \t' +str(record[3])+ '   \t' +str(record[4])+"\n\n"
    query_label = CTkLabel(P,text=print_record,font=("century gothic",15))
    query_label.place(x=40,y=40)
    # query_label.grid(row=14,column=0,columnspan=2)
    conn.commit()
    conn.close()

    P.mainloop()


show_all_btn = CTkButton(frame5,text='SHOW ALL',fg_color='teal',hover_color="royalblue",font=('century goyhic',20),text_color='black',height=50,width=200,command=query)
show_all_btn.place(x=805,y=26)

closetab_btn = CTkButton(frame5,text='CLOSE',fg_color='teal',hover_color="firebrick",font=('century goyhic',20),text_color='black',height=50,width=200,command=closetab)
closetab_btn.place(x=1030,y=26)


switch_var = StringVar(value="light")
def switch_event():
    set_appearance_mode(switch_var.get())

dark_switch = CTkSwitch(loginP, text="Dark mode",font=("Century Gothic",15),button_color='lightgrey',progress_color='dimgrey', command=switch_event,variable=switch_var, onvalue="dark", offvalue="light")
dark_switch.pack(anchor='s',side='left',padx=15)

tail1 = CTkLabel(loginP, text=(time.asctime()),text_color=('black',"white"),font=("century gothic",11))
tail1.pack(side=RIGHT,anchor='n',padx=10)

loginP.mainloop()
