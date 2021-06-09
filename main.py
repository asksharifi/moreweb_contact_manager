from tkinter import *
import pymysql as mysql
from tkinter.ttk import Combobox, Treeview
import connectit as cnf
from time import sleep
from threading import Thread
from tkinter import messagebox
app = Tk()
app.title('Contacts')


def get_about_text():
    about_txt = open()


def __init__():
    pass


def run_trv(win_name):
    global tv
    tv = Treeview(win_name)
    tv['columns'] = ("name", "lname", "email", "phone", "comment")
    tv['show'] = "headings"
    tv.heading(0, text="Name")
    tv.heading(0, text="Name")
    tv.heading(1, text="Last name")
    tv.heading(2, text="E-mail")
    tv.heading(3, text="Phone number")
    tv.heading(4, text="Comments")
    print("Treeview loded")


def run_trv1(win_name):
    global tv1
    tv1 = Treeview(win_name)
    tv1['columns'] = ("name", "lname", "phone", "email", "fax", "comment")
    tv1['show'] = "headings"
    tv1.heading(0, text="Name")
    tv1.heading(1, text="Last name")
    tv1.heading(2, text="Phone number")
    tv1.heading(3, text="E-mail")
    tv1.heading(4, text="Fax")
    tv1.heading(5, text="Comments")

    print("Treeview loded")


def run_trv_ins(win_name):
    global tvins
    tvins = Treeview(win_name)
    tvins['columns'] = ("name", "lname", "email", "phone", "comment")
    tvins['show'] = "headings"
    tvins.heading(0, text="Name")
    tvins.heading(1, text="Last name")
    tvins.heading(2, text="E-mail")
    tvins.heading(3, text="Phone number")
    tvins.heading(4, text="Comments")

    print("Treeview loded")


run_trv(app)
tv.grid(row=1, column=1, columnspan=6) 
verscrlbar = Scrollbar(app, orient="vertical", command=tv.yview)
verscrlbar.grid(row=1, column=0)
cn = cnf.cn
cr = cnf.cr
get_all_in_table = "select * from moreweb_cm"
gain_qe = cr.execute(get_all_in_table)
all_items_list = cr.fetchall()
for i in all_items_list:
    tv.insert("", "end", values=(i[1], i[2], i[3], i[4], i[5]))
    print(i)


def autoload():
    cn = cnf.cn
    cr = cnf.cr
    while True:
        get_all_in_table = "select * from moreweb_cm"
        gain_qe = cr.execute(get_all_in_table)
        all_items_list = cr.fetchall()
        a = tv.get_children()
        for i in a:
            tv.delete(i)
        for i in all_items_list:
            tv.insert("", "end", values=(i[1], i[2], i[3], i[4], i[5]))
        sleep(10)


atl_thread_s = Thread(target=autoload, args=())
atl_thread_s.start()


def insert_data():
    try:
        def insert_command_btnc():
            name_v = ename.get()
            lname_v = elname.get()
            email_v = eemail.get()
            phone_v = ephone.get()
            cmnt_v = ecmnt.get()
            value_list = (name_v, lname_v, email_v, int(phone_v), cmnt_v)

            q_insert = "insert into moreweb_cm (Cn,cln,email,phone,comment) VALUES (%s,%s,%s,%s,%s)"
            cr.execute(q_insert, value_list)
            print(i)
            tvins.insert("", "end", values=(
                name_v, lname_v, email_v, phone_v, cmnt_v))
    except:
        messagebox.ERROR("Sothing repeated")
    insert_win = Toplevel()
    insert_win.resizable(0, 0)

    run_trv_ins(insert_win)
    tvins.grid(row=0, column=0, rowspan=5, columnspan=6)
    lname = Label(insert_win, text="Name:")
    ename = Entry(insert_win)
    lname.grid(row=7, column=0)
    ename.grid(row=7, column=1)
    llname = Label(insert_win, text="Last Name:")
    elname = Entry(insert_win)
    llname.grid(row=7, column=2)
    elname.grid(row=7, column=3)
    lemail = Label(insert_win, text="E-mail:")
    eemail = Entry(insert_win)
    lemail.grid(row=8, column=0)
    eemail.grid(row=8, column=1)
    lphone = Label(insert_win, text="Phone number:")
    ephone = Entry(insert_win)
    lphone.grid(row=8, column=2)
    ephone.grid(row=8, column=3)
    lcmnt = Label(insert_win, text="Note/About:")
    ecmnt = Entry(insert_win)
    lcmnt.grid(row=9, column=2)
    ecmnt.grid(row=9, column=3)
    submit_btn = Button(insert_win, text="Add number",
                        command=insert_command_btnc)
    submit_btn.grid(row=9, column=4)


def update_data():
    edit_win = Toplevel()
    ledby = Label(edit_win, text="ٍEdit by:")
    cbedby = Combobox(edit_win, value=[
                      "Name", "Last Name", "E-mail", "Phone number"], state="readonly")
    cbedby.set("Phone number")
    ledby.grid(row=0, column=0)
    cbedby.grid(row=0, column=1)
    lcurval = Label(edit_win, text="Current Phone number:")
    ecurval = Entry(edit_win)
    lcurval.grid(row=1, column=0)
    ecurval.grid(row=1, column=1)
    lnewval = Label(edit_win, text="New Phone number:")
    enewval = Entry(edit_win)
    lnewval.grid(row=2, column=0)
    enewval.grid(row=2, column=1)

    def autoset_ltext():
        while True:
            cb_get_v = cbedby.get()
            lcurval.config(text=f"Current {cb_get_v}:")
            lnewval.config(text=f"new {cb_get_v}:")
            sleep(0.5)
    autoset_thr = Thread(target=autoset_ltext)
    autoset_thr.start()
    def update_btnc():
        cb
    Submit_btn = Button(edit_win,text="        Update Contact        ")
    Submit_btn.grid(row=3,column=1)



def delete_data():
    pass


def loader():
    get_all_in_table = "select * from moreweb_cm"
    gain_qe = cr.execute(get_all_in_table)
    all_items_list = cr.fetchall()
    a = tv.get_children()
    for i in a:
        tv.delete(i)
    for i in all_items_list:
        tv.insert("", "end", values=(i[1], i[2], i[3], i[4], i[5]))
    print("kardam dadash!!")


# buttons
insert_btn = Button(app, text="Add..", command=insert_data)
update_btn = Button(app, text="Edit", command=update_data)
del_btn = Button(app, text="Remove")
Ref_btn = Button(app, text="Refresh", command=loader)
insert_btn.grid(row=2, column=0, columnspan=1)
update_btn.grid(row=3, column=0)
del_btn.grid(row=4, column=0)
Ref_btn.grid(row=5, column=0)
app.mainloop()
