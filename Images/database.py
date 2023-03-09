from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title = ("Learn Coding")
root.iconbitmap("./Images/mytkico.ico")
root.geometry("400x500")

#Databases

#Create a database or connect to one
conn = sqlite3.connect("address_book.db")

#Create cursor - c
c = conn.cursor()

#Create table
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )

# """)

#Create Edit function to update a record

def update():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor - c
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'address':address_editor.get(),
        'city':city_editor.get(),
        'state':state_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
        })

    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    delete_box.delete(0,END)

    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title = ("Update a Record")
    editor.iconbitmap("./Images/mytkico.ico")
    editor.geometry("400x250")
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor - c
    c = conn.cursor()

    record_id = delete_box.get()

    #Query the database
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    records = c.fetchall()

    #Create Global Variables for text box names
    global f_name_editor,\
    l_name_editor,\
    address_editor,\
    city_editor,\
    state_editor,\
    zipcode_editor

    #Create Text Boxes
    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    city_editor = Entry(editor,width=30)
    city_editor.grid(row=3,column=1)
    state_editor = Entry(editor,width=30)
    state_editor.grid(row=4,column=1)
    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)



    #Create Text Box Labels
    f_name_label = Label(editor,text="First Name:")
    f_name_label.grid(row=0,column=0,pady=(10,0),sticky=W)
    l_name_label = Label(editor,text="Last Name:")
    l_name_label.grid(row=1,column=0,sticky=W)
    address_label = Label(editor,text="Address:")
    address_label.grid(row=2,column=0,sticky=W)
    city_label = Label(editor,text="City:")
    city_label.grid(row=3,column=0,sticky=W)
    state_label = Label(editor,text="State:")
    state_label.grid(row=4,column=0,sticky=W)
    zipcode_label = Label(editor,text="Zipcode:")
    zipcode_label.grid(row=5,column=0,sticky=W)

    # Loop Through Results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5]) 

    #Create a Save Button To save edited record
    save_btn = Button(editor,text="Save Record",command=update)
    save_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=145)


#Create Submit Function For Database
def submit():
 
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor - c
    c = conn.cursor()

    #Insert Into Table 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    })

    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()

    #Clear The Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor - c
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    # print(records)
    # Loop Through Results
    # print_records = ''

    queryRecord = Tk()
    queryRecord.iconbitmap("./Images/mytkico.ico")
    queryRecord.geometry("600x400")

    queryRecordFrame = LabelFrame(queryRecord,padx=20,pady=5)
    queryRecordFrame.pack(padx=10,pady=10)

        #Create Text Box Labels
    f_q_label = Label(queryRecordFrame,text="First Name")
    f_q_label.grid(row=0,column=0,padx=(0,10),sticky=W)
    l_q_label = Label(queryRecordFrame,text="Last Name")
    l_q_label.grid(row=0,column=1,padx=(0,10),sticky=W)
    address_q_label = Label(queryRecordFrame,text="Address")
    address_q_label.grid(row=0,column=2,padx=(0,10),sticky=W)
    city_q_label = Label(queryRecordFrame,text="City")
    city_q_label.grid(row=0,column=3,padx=(0,10),sticky=W)
    state_q_label = Label(queryRecordFrame,text="State")
    state_q_label.grid(row=0,column=4,padx=(0,10),sticky=W)
    zipcode_q_label = Label(queryRecordFrame,text="Zipcode")
    zipcode_q_label.grid(row=0,column=5,sticky=W)
    oid_q_label = Label(queryRecordFrame,text="Id")
    oid_q_label.grid(row=0,column=6,padx=(10,0),sticky=W)

    rowstart = 1

    for record in records:
        # print_records += "" + str(record[0]) + " " + str(record[1]) + "  " + " " + str(record[6]) + '\n'
        f_query_label = Label(queryRecordFrame,text=str(record[0]))
        f_query_label.grid(row=rowstart,column=0,padx=(0,10),sticky=W)
        l_query_label = Label(queryRecordFrame,text=str(record[1]))
        l_query_label.grid(row=rowstart,column=1,padx=(0,10),sticky=W)
        address_query_label = Label(queryRecordFrame,text=str(record[2]))
        address_query_label.grid(row=rowstart,column=2,padx=(0,10),sticky=W)
        city_query_label = Label(queryRecordFrame,text=str(record[3]))
        city_query_label.grid(row=rowstart,column=3,padx=(0,10),sticky=W)
        state_query_label = Label(queryRecordFrame,text=str(record[4]))
        state_query_label.grid(row=rowstart,column=4,padx=(0,10),sticky=W)
        zipcode_query_label = Label(queryRecordFrame,text=str(record[5]))
        zipcode_query_label.grid(row=rowstart,column=5,padx=(0,10),sticky=W)
        oid_query_label = Label(queryRecordFrame,text=str(record[6]))
        oid_query_label.grid(row=rowstart,column=6,padx=(10,0),sticky=W)
        rowstart+=1
    exit_query_btn = Button(queryRecordFrame,text="Exit",command=queryRecord.destroy)
    exit_query_btn.grid(row=rowstart,column=0,columnspan=6,ipadx=40)


    
    # query_label = Label(root, text=print_records)
    # query_label.grid(row=12,column=0,columnspan=2)

    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()

def delete():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor - c
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())


    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    delete_box.delete(0,END)

#Create Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
address = Entry(root,width=30)
address.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)


#Create Text Box Labels
f_name_label = Label(root,text="First Name:")
f_name_label.grid(row=0,column=0,pady=(10,0),sticky=W)
l_name_label = Label(root,text="Last Name:")
l_name_label.grid(row=1,column=0,sticky=W)
address_label = Label(root,text="Address:")
address_label.grid(row=2,column=0,sticky=W)
city_label = Label(root,text="City:")
city_label.grid(row=3,column=0,sticky=W)
state_label = Label(root,text="State:")
state_label.grid(row=4,column=0,sticky=W)
zipcode_label = Label(root,text="Zipcode:")
zipcode_label.grid(row=5,column=0,sticky=W)
delete_box_label = Label(root,text = "Select ID:")
delete_box_label.grid(row=9,column=0,sticky=W)

#Create Submit Button
submit_btn = Button(root,text="Add Record To Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=109)

#Create a Query Button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a Delete Button
delete_btn = Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=138)

#Create an Update Button
edit_btn = Button(root,text="Edit Record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=144)

#Commit Changes
conn.commit()

#Close connection
conn.close()

exit_btn = Button(root,text="Exit",command=root.destroy)
exit_btn.grid(row=12,column=0,columnspan=6,ipadx=40)

root.mainloop()