from tkinter import *
from backend import Database

#creating object from database class
database = Database("books.db")

#function to take values from backed insert function and put the values into frontend listbox
def view_command():
    list1.delete(0, END) #delete everything from the listbox till the END to not add the same rows again and again after clicking "view all" multiple times
    for row in database.view():
        list1.insert(END, row)  #END -> adding new values always in the end

#function to take values from Entry fields, pass them to database search function and print results in listbox
def search_command():
    list1.delete(0, END)
    for row in database.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)

#function which take values from Entry fields, pass them to database insert function and add new row to database
def insert_command():
    list1.delete(0, END)
    database.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    list1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))

#function to select information from listbox when clicking on a row, function connected with list1.bind('<<<Listbox>>>', get_selected_row) method
#used also to fill the entry areas with the information taken from clicked row
def get_selected_row(event):
    try:
        global selected_tuple # define as global variable (can be used outside of the function)
        index=list1.curselection()[0] #returning the index of clicked row from listbox
        selected_tuple=list1.get(index) #returning the tuple (row) with this index

        #fill the empty entry areas with the information from clicked row
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    
    except IndexError:
        pass

#exception was used to solve an error - when the listbox is empty and user clicks on it the program has an error because 
#get_selected_row function is looking for a [0] of a row but it does not exist
#when error appears none of the lines below ' try: ' will be executed, 
#line under except will be executed -> pass which means that function does nothing in this case


#function which takes id of selected tuple (from get_selected_row function) and passes it to database.delete
def delete_command():
    database.delete(selected_tuple[0])
    view_command() #calling this function to see the updated view immediately after deleting row

#function which takes values from entry areas and updates the row
def update_command():
    database.update(selected_tuple[0],title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()
   
#creating desktop window
window = Tk() 
window.title("BookStore")

#adding label areas
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Year')
l2.grid(row=1, column=0)

l3 = Label(window, text='Author')
l3.grid(row=0, column=2)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

#adding entry areas
title_value = StringVar()
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0,column=1)

year_value = StringVar()
e2 = Entry(window, textvariable=year_value)
e2.grid(row=1,column=1)

author_value = StringVar()
e3 = Entry(window, textvariable=author_value)
e3.grid(row=0,column=3)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1,column=3)

# adding buttons
b1 = Button(window, text = 'View All', width=15, command = view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text = 'Search entry', width=15, command = search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text = 'Add entry', width=15, command = insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text = 'Update', width=15, command = update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text = 'Delete', width=15, command = delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text = 'Close', width=15, command = window.destroy)
b6.grid(row=7, column=3)

#adding text window
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#adding scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan=6)

#joining scrollbar with listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#method to bind a function to a widget event, to take values from the tuple in the list
list1.bind('<<ListboxSelect>>', get_selected_row)

#displaying the window all the time
window.mainloop()

