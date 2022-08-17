from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.title("Class Activity 173")
root.geometry("500x500")

burger = ImageTk.PhotoImage(Image.open("burger.jpg"))
burger_image = Label(root, image = burger)
burger_image.place(relx = 0.7, rely = 0.5, anchor = CENTER)
label_heading = Label(root, text = "Two Sided", fg = "grey", bg = "white", font = ("times",25))
label_heading.place(relx = 0.12, rely = 0.1, anchor = CENTER)
label_dish = Label(root, text = "Select your dish.", font = ("times",10))
label_dish.place(relx = 0.06, rely = 0.2, anchor = CENTER)
dish_list = ["Burger", "Strawberry Passionfruit Limonita"]
dish_dropdown = ttk.Combobox(root, state = "readonly", values = dish_list)
dish_dropdown.place(relx = 0.25, rely = 0.2, anchor = CENTER)
label_add_ons = Label(root, text = "Choose your add-ons", font = ("times",10))
label_add_ons.place(relx = 0.07, rely = 0.5, anchor = CENTER)
add_ons_list = []
add_ons_dropdown = ttk.Combobox(root, state = "readonly", values = add_ons_list)
add_ons_dropdown.place(relx = 0.25, rely = 0.5, anchor = CENTER)
dish_price = Label(root, font = ("times",15,"bold"))
dish_price.place(relx = 0.2, rely = 0.75, anchor = CENTER)

class parent :
    def __init__(self) :
        print("This is a parent class")
        
    def menu(dish) :
        if dish == "Burger" :
            print("You can add the following toppings")
            add_ons_list = ["Extra Cheese", "Jalpenos"]
            add_ons_dropdown["values"] = add_ons_list
            print("Extra Cheese and/or Jalpenos")
            
        elif dish == "Strawberry Passionfruit Limonita" :
            print("You can add the following toppings for your drink.")
            add_ons_list = ["Extra Strawberry", "Rasberry Flavoring"]
            add_ons_dropdown["values"] = add_ons_list
            print("Extra Strawberry and/or Rasberry Flavoring")
            
        else :
            print("Please enter a valid dish.")
            
    def end_bill(dish, add_ons) :
        if dish == "Burger" and add_ons == "Extra Cheese" :
            dish_price["text"] = "Amount Due : $7.00"
            print("Amount due : $7.00")
            
        elif dish == "Burger" and add_ons == "Jalpenos" :
            dish_price["text"] = "Amount Due : $6.50"
            print("Amount due : $6.50")
            
        elif dish == "Strawberry Passionfruit Limonita" and add_ons == "Extra Strawberry" :
            dish_price["text"] = "Amount Due : $10.00"
            print("Amount due : $10.00")
            
        elif dish == "Strawberry Passionfruit Limonita" and add_ons == "Rasberry Flavoring" :
            dish_price["text"] = "Amount Due : $12.50"
            print("Amount due : $12.50")
            
class child(parent) :
    def __init__(self, dish) :
        self.dish = dish
        
    def get_menu(self) :
        new_dish = dish_dropdown.get()
        parent.menu(new_dish)

class child2(parent) :
    def __init__(self, dish, add_ons) :
        self.new_dish = dish
        self.add_ons = add_ons
        
    def final_bill(self) :
        new_dish = dish_dropdown.get()
        addons = add_ons_dropdown.get()
        parent.end_bill(new_dish, addons)
        
obj1 = child(dish_dropdown.get())
obj1.get_menu()
obj2 = child2(add_ons_dropdown.get(), dish_dropdown.get())
obj2.final_bill()
btn_addons = Button(root, text = "Addon options.", command = obj1.get_menu(), bg = "blue", fg = "white", relief = FLAT)
btn_addons.place(relx = 0.06, rely = 0.3, anchor = CENTER)
btn_amount = Button(root, text = "Amount due.", command = obj2.final_bill(), bg = "blue", fg = "white", relief = FLAT)
btn_amount.place(relx = 0.04, rely = 0.6, anchor = CENTER)
root.mainloop()