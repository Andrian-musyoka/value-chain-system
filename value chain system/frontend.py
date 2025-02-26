import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk



def submit_data():
    farmer = farmer_entry.get()
    farmerIdNO = farmer_entry.get()
    farmLocation = farmLocation_entry.get()
    password = password_entry.get()
    
    if not (farmer and farmerIdNO and farmLocation and password):
        messagebox.showwarning("Input Error", "All fields must be filled!")
        return
    
    summary_text.set(f"Farmer: {farmer}\nProcessor: {farmerIdNO}\nDistributor: {farmLocation}\nRetailer: {password}")
    messagebox.showinfo("Success", "Data Submitted Successfully!")

# Main application window
window= tk.Tk()
window.title("Coffee Value Chain Interface")
window.geometry("1000x1000")
window.configure(bg="yellow")

image = Image.open(r"C:\Users\san\Desktop\value chain system\coffeeCup.jpg")
bg_image = ImageTk.PhotoImage(image)

label_bg = tk.Label(window, image=bg_image)
label_bg.place(relwidth=1, relheight=1)


# Title Label
title_label = ttk.Label(window, text="Coffee Value Chain", font=("arial black", 20))
title_label.pack(pady=10)

# Frame for input fields
frame = ttk.Frame(window, padding=10)
frame.pack(pady=10, fill=tk.X) 

# Farmer Input
farmer_label = ttk.Label(frame, text="Farmer Name:")
farmer_label.grid(row=0, column=0, padx=5, pady=5)
farmer_entry = ttk.Entry(frame, width=40)
farmer_entry.grid(row=0, column=1, padx=5, pady=5)

# Farmer id number Input
farmerIdNO_label = ttk.Label(frame, text="Farmer's ID N.O:")
farmerIdNO_label.grid(row=1, column=0, padx=5, pady=5)
farmer_entry = ttk.Entry(frame, width=40)
farmer_entry.grid(row=1, column=1, padx=5, pady=5)

# Farmer's farm location
farmLocation_label = ttk.Label(frame, text="Farm location:")
farmLocation_label.grid(row=2, column=0, padx=5, pady=5)
farmLocation_entry = ttk.Entry(frame, width=40)
farmLocation_entry.grid(row=2, column=1, padx=5, pady=5)

# Farmer's password
password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=3, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame, width=40)
password_entry.grid(row=3, column=1, padx=5, pady=10)

# logIn Button
logIn_button = ttk.Button(window, text="Log In", command=submit_data)
logIn_button.pack(pady=10)

# Summary Section
summary_text = tk.StringVar()
summary_label = ttk.Label(window, textvariable=summary_text, relief=tk.SUNKEN, padding=10)
summary_label.pack(pady=10, fill=tk.X)

# Run Application
window.mainloop()
