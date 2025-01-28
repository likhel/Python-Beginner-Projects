'''from tkinter import *

window = Tk()

def submit():
    food = []

    print("you have ordered:")

    for i in listbox.curselection():
       food.insert(i,listbox.get(i))

    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height = listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height = listbox.size())

listbox = Listbox(window,
                  bg = "yellow",
                  font = ("Cursive,30"),
                  width = 12,
                  selectmode = MULTIPLE  )

listbox.insert(1,"samosa")
listbox.insert(2,"aluchana")
listbox.insert(3,"pakoda")
listbox.insert(4,"aluchop")
listbox.pack()

entrybox = Entry(window)
entrybox.pack()

submit_button = Button(window, text = "Submit", command = submit )
submit_button.pack()

delete_button = Button(window, text = "Delete", command = delete)
delete_button.pack()

add_button = Button(window, text = "Add", command = add)
add_button.pack()

window.mainloop()'''

from tkinter import *

def submit():
    food = []
    print("You have ordered:")
    for i in listbox.curselection():
        food.append(listbox.get(i))
        print(listbox.get(i))
    
    for i in food:
        print(i)

def add():
    item = entrybox.get()
    if item.strip() != "":  # Check if entry is not empty
        listbox.insert(END, item)
        listbox.config(height=listbox.size())

def delete():
    selected_indices = listbox.curselection()
    for i in reversed(selected_indices):
        listbox.delete(i)
    listbox.config(height=listbox.size())

window = Tk()
window.title("Food Ordering System")

# Listbox for food items
listbox = Listbox(window, bg="yellow", font=("Arial", 12), width=20, selectmode=MULTIPLE)
listbox.pack(padx=10, pady=10)

# Entry for adding new items
entrybox = Entry(window, font=("Arial", 12), width=20)
entrybox.pack(padx=10, pady=5)

# Buttons
submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(padx=10, pady=5)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(padx=10, pady=5)

add_button = Button(window, text="Add", command=add)
add_button.pack(padx=10, pady=5)

window.mainloop()


