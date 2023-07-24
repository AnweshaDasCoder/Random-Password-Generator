from tkinter import *
import random

root=Tk()
root.title("Geberate a Password")
root.geometry("400x400")

array_3d = [[['#', '$', '*', '&', '%', '@', '^', '!', '?'], ["Jack", "Joker", "Queen", "King"],["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]]

def input_password():
    label["text"] = "Old Password: " + entry.get()
    
def new_password():
    random_no_1 = random.randint(0,8)
    random_no_2 = random.randint(0,3)
    random_no_3 = random.randint(0,25)
        
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    label1["text"] ="New Password: " + letter1 + "" + letter2 + "" +letter3

entry = Entry(root)
entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)

btn = Button(root, text = "Input Your Password", command = input_password)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text="Old Password: ")
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn1 = Button(root, text = "New Password", command = new_password)
btn1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label1 = Label(root, text="New Password: ")
label1.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

