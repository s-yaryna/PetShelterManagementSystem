#PROJECT 1 - PET SHELTER MANAGEMENT SYSTEM
import tkinter as tk
from tkinter import Toplevel, Entry, Label, Button, ttk, messagebox
from turtle import left, width

# ========== Animal database ==========
animals = []

# ========== PARENT CLASS ==========
class Animal:
    #properties
    def __init__(self, animal_id, animal_type, animal_name, animal_age, room_number, feeding_status, playing_status):
        self.animal_id = animal_id
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.animal_age = animal_age
        self.room_number = room_number
        self.feeding_status = feeding_status
        self.playing_status = playing_status

    #storing animal information
    def store_animal(self):
        return [
            self.animal_id,
            self.animal_type,
            self.animal_name,
            self.animal_age,
            self.room_number,
            self.feeding_status,
            self.playing_status
        ]

class Error:
    def __init__(self, error_title, error_description):
        self.error_title = error_title
        self.error_description = error_description

# ========== CHILDREN CLASSES ==========
class Mammal(Animal):
    animal_food = " snacks: Meat"
    animal_toy = " red ball"

class Fish(Animal):
    animal_food = " snacks: Grass"
    animal_toy = " green ball"

class Bird(Animal):
    animal_food = " snacks: Corn"
    animal_toy = " yellow ball"

class Animal_Type(Error):
    error_title = "Important notification!"
    error_description = "The wrong type of pet is entered.\nAccepted values: Mammal, Fish, Bird. \nTry again"
    
    def __init__(self):
        super().__init__(Animal_Type.error_title, Animal_Type.error_description)

class Animal_Feeding_Status(Error):
    error_title = "Important notification!"
    error_description = "The pet needs to eat. Feed the animal.\nThe suitable food for this animal is -> "
    
    def __init__(self):
        super().__init__(Animal_Feeding_Status.error_title, Animal_Feeding_Status.error_description)

class Animal_Playing_Status(Error):
    error_title = "Important notification!"
    error_description = "The pet needs to play. Play with animal.\nThe suitable toy for this animal is -> "
    
    def __init__(self):
        super().__init__(Animal_Playing_Status.error_title, Animal_Playing_Status.error_description)

# ========== Screen 1 ==========
#screen 1 = database
#screen 2 = add form
screen_1 = tk.Tk()
screen_1.title('Pet Shelter Management System')
screen_1.geometry("1500x1080")
screen_1.configure(bg="#3E482A")

def open_screen_2():
    screen_2 = tk.Toplevel(screen_1)
    screen_2.title('Add new animal')
    screen_2.geometry("600x1000")
    screen_2.configure(bg = "#79804D")
    
    screen2_title_1 = Label(screen_2, text='Add new animal', height=3, bg="#79804D", fg="white", font=("Tahoma", 24))
    screen2_title_1.pack()
    
    #Adding and creating form (labels + inputs)
    animal_id_lable = Label(screen_2, text="ID Number:", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    animal_id = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    animal_id_lable.pack()
    animal_id.pack()
    
    animal_type_lable = Label(screen_2, text="Type: (Mammal/Fish/Bird)", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    animal_type = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    animal_type_lable.pack()
    animal_type.pack()
    
    animal_name_lable = Label(screen_2, text="Name:", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    animal_name = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    animal_name_lable.pack()
    animal_name.pack()
    
    animal_age_lable = Label(screen_2, text="Age:", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    animal_age = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    animal_age_lable.pack()
    animal_age.pack()
    
    room_number_lable = Label(screen_2, text="Room number:", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    room_number = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    room_number_lable.pack()
    room_number.pack()
    
    feeding_status_lable = Label(screen_2, text="Feeding_status (True/False):", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    feeding_status = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    feeding_status_lable.pack()
    feeding_status.pack()
    
    playing_status_lable = Label(screen_2, text="Playing_status:", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
    playing_status = Entry(screen_2, width=45, bg="#2D2920", fg="white", font=("Tahoma", 13), justify="left")
    playing_status_lable.pack()
    playing_status.pack()
    
    def add_data_animal():
        #validation of animal type
        if animal_type.get() not in ["Mammal", "Fish", "Bird"]:
            error = Animal_Type()
            screen_error = tk.Toplevel(screen_2)
            screen_error.title("Error: Type of pet")
            screen_error.geometry("400x250")
            screen_error.configure(bg="#69573B")
            
            error_title_lable = Label(screen_error, text=error.error_title, height=3, bg="#69573B", fg="white", font=("Tahoma", 15, "bold"))
            error_description_lable = Label(screen_error, text=error.error_description, height=3, bg="#69573B", fg="white", font=("Tahoma", 13))
            try_again_button = tk.Button(screen_error, text='Try again', width=23, height=1, bg='#79804D', fg="white", font="Tahoma", command=screen_error.destroy)
            
            error_title_lable.pack()
            error_description_lable.pack()
            try_again_button.pack()
            return
            
        #feeding status validation
        elif feeding_status.get() == "False":
            error = Animal_Feeding_Status()
            animals_classes = {"Mammal": Mammal, "Fish": Fish, "Bird": Bird}
            food = animals_classes[animal_type.get()].animal_food
            message = str(error.error_description + food)
            
            screen_error = tk.Toplevel(screen_2)
            screen_error.title("Error: Feed the pet")
            screen_error.geometry("400x250")
            screen_error.configure(bg="#69573B")
            
            error_title_lable = Label(screen_error, text=error.error_title, height=3, bg="#69573B", fg="white", font=("Tahoma", 15, "bold"))
            error_description_lable = Label(screen_error, text=message, height=3, bg="#69573B", fg="white", font=("Tahoma", 13))
            feed_button = tk.Button(screen_error, text='Feed', width=23, height=1, bg='#79804D', fg="white", font="Tahoma", command=screen_error.destroy)
            
            error_title_lable.pack()
            error_description_lable.pack()
            feed_button.pack()
            return
            
        #playing status validation
        elif playing_status.get() == "False":
            error = Animal_Playing_Status()
            animals_classes = {"Mammal": Mammal, "Fish": Fish, "Bird": Bird}
            toy = animals_classes[animal_type.get()].animal_toy
            message = str(error.error_description + toy)
            
            screen_error = tk.Toplevel(screen_2)
            screen_error.title("Error: Play with pet")
            screen_error.geometry("400x250")
            screen_error.configure(bg="#69573B")
            
            error_title_lable = Label(screen_error, text=error.error_title, height=3, bg="#69573B", fg="white", font=("Tahoma", 15, "bold"))
            error_description_lable = Label(screen_error, text=message, height=3, bg="#69573B", fg="white", font=("Tahoma", 13))
            play_button = tk.Button(screen_error, text='Play', width=23, height=1, bg='#79804D', fg="white", font="Tahoma", command=screen_error.destroy)
            
            error_title_lable.pack()
            error_description_lable.pack()
            play_button.pack()
            return

        new_pet = Animal(animal_id.get(), animal_type.get(), animal_name.get(), animal_age.get(), room_number.get(), feeding_status.get(), playing_status.get())
        animals.append(new_pet)
        rows.insert("", tk.END, values=new_pet.store_animal())
        
        #successfully adding pet window
        screen_notification = tk.Toplevel(screen_2)
        screen_notification.title("Pet added")
        screen_notification.geometry("400x250")
        screen_notification.configure(bg="#79804D")
        
        screen_notification_title_lable = Label(screen_notification, text="Important notification!", height=3, bg="#79804D", fg="white", font=("Tahoma", 15, "bold"))
        screen_notification_description_lable = Label(screen_notification, text="The pet successfully added to the system", height=3, bg="#79804D", fg="white", font=("Tahoma", 13))
        ok_button = tk.Button(screen_notification, text='Ok', width=23, height=1, bg='#69573B', fg="white", font="Tahoma", command=screen_2.destroy)

        remove_database_button["state"] = "normal"
        screen_notification_title_lable.pack()
        screen_notification_description_lable.pack()
        ok_button.pack()

    add_button = tk.Button(screen_2, text='Add', width=23, height=2, bg='#2D2920', fg="white", font="Tahoma", command=add_data_animal)
    empty_lable = Label(screen_2, text="", height=2, bg="#79804D", fg="white", font=("Tahoma", 13))

    empty_lable.pack()
    add_button.pack()
    empty_lable.pack()

def remove_database_item():
    screen_remove_message = tk.Toplevel(screen_1)
    screen_remove_message.title("Remove pet")
    screen_remove_message.geometry("400x250")
    screen_remove_message.configure(bg="#2D2920")
    
    screen_remove_message_title_label = Label(screen_remove_message, text="Remove pet", height=3, bg="#2D2920", fg="white", font=("Tahoma", 15, "bold"))
    screen_remove_message_label = Label(screen_remove_message, text="ID Number:", height=3, bg="#2D2920", fg="white", font=("Tahoma", 13))
    screen_remove_message_id = Entry(screen_remove_message, width=35, bg="#69573B", fg="white", font=("Tahoma", 13), justify="left")
    
    def remove_by_id():
        remove_id = screen_remove_message_id.get().strip()
        check_id = False
        checking_animals = []
        global animals
        
        for pet in animals:
            if str(pet.animal_id).strip() == remove_id:
                check_id = True
            else:
                checking_animals.append(pet)
                
        if not check_id:
            messagebox.showinfo("Wrong ID", f"No pets with this ID -> {remove_id}")
            return
            
        animals = checking_animals
        for item in rows.get_children():
            if str(rows.item(item)['values'][0]).strip() == remove_id:
                rows.delete(item)
                break
        screen_remove_message.destroy()
        
    remove_button = tk.Button(screen_remove_message, text='Remove', width=23, height=1, bg='#69573B', fg="white", font="Tahoma", command=remove_by_id)
    empty_lable = Label(screen_remove_message, text="", height=1, bg="#2D2920", fg="white", font=("Tahoma", 13))

    screen_remove_message_title_label.pack()
    screen_remove_message_label.pack()
    screen_remove_message_id.pack()
    empty_lable.pack()
    remove_button.pack()

# Screen 1: Section 1
section_1 = tk.Frame(screen_1, bg="#2D2920", height=400, pady=40)
screen1_title_1 = Label(section_1, text='Pet management system', height=3, bg="#2D2920", fg="white", font=("Tahoma", 28))
add_animal_button = tk.Button(section_1, text='Add new animal', width=23, height=2, bg='#79804D', fg="white", font="Tahoma", command=open_screen_2)
section_1.pack(fill="both", expand=True)
screen1_title_1.pack()
add_animal_button.pack()

# Screen 1: Section 2
section_2 = tk.Frame(screen_1, bg="#3E482A", height=300, pady=40)
screen1_title_2 = Label(section_2, text='Database', height=3, bg='#3E482A', fg="white", font=("Tahoma", 28))
remove_database_button = tk.Button(section_2, state="disabled", text='Remove', width=23, height=2, bg='#79804D', fg="white", font="Tahoma", command=remove_database_item)
section_2.pack(expand=True)
screen1_title_2.pack()
remove_database_button.pack()

# Screen 1: Section 3 - Database
database_style = ttk.Style()
database_style.theme_use("default")
database_style.configure("Treeview.Heading", background="#2D2920", foreground="white", font=("Tahoma", 14, "bold"))
database_style.configure("Treeview", background="#79804D", fieldbackground="#79804D", foreground="white", font=("Tahoma", 12))

colomns = ("ID", "Type", "Name", "Age(Years)", "Room number", "Feeding status", "Playing status")
rows = ttk.Treeview(screen_1, columns=colomns, show="headings")
for colomn in colomns:
    rows.heading(colomn, text=colomn)
    rows.column(colomn)
rows.pack(pady=20, expand=True)

screen_1.mainloop()
