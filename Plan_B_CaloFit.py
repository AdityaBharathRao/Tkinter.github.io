# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:33:38 2024

@author: Aditya
"""

import tkinter as tk
from tkinter import ttk

class CaloFit:
    def __init__(self, root):
        self.root = root
        self.root.title("CaloFit")
        self.root.configure(bg="#404040")
        
        
        
        self.meals = []
        self.total_calories = 0

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#f0f0f0", borderwidth=2, relief="groove", padding=10)
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        self.style.configure("TButton", background="#4287f5", foreground="white", font=("Helvetica", 10))
        self.style.map("TButton", background=[("active", "#3c73c8")])
        self.style.configure("Treeview", background="white", fieldbackground="#f0f0f0", font=("Helvetica", 10), rowheight=25)

        self.title_label = ttk.Label(root, text="CaloFit", font=("Helvetica", 24, "bold"), background="#f0f0f0")
        self.title_label.pack(pady=(20, 10))

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.add_meal_frame = ttk.Frame(self.main_frame)
        self.add_meal_frame.pack(pady=10)

        self.meal_label = ttk.Label(self.add_meal_frame, text="Meal:", background="#f0f0f0")
        self.meal_label.grid(row=0, column=0, padx=5)

        self.meal_entry = ttk.Entry(self.add_meal_frame, width=30)
        self.meal_entry.grid(row=0, column=1, padx=5)

        self.calories_label = ttk.Label(self.add_meal_frame, text="Calories:", background="#f0f0f0")
        self.calories_label.grid(row=0, column=2, padx=5)

        self.calories_entry = ttk.Entry(self.add_meal_frame, width=10)
        self.calories_entry.grid(row=0, column=3, padx=5)

        self.add_button = ttk.Button(self.add_meal_frame, text="Add", command=self.add_meal)
        self.add_button.grid(row=0, column=4, padx=10)

        self.table_frame = ttk.Frame(self.main_frame)
        self.table_frame.pack()

        self.table = ttk.Treeview(self.table_frame, columns=("Meal", "Calories"), show="headings")
        self.table.heading("Meal", text="Meal")
        self.table.heading("Calories", text="Calories")
        self.table.pack(pady=10, padx=10, fill="both", expand=True)

        self.total_calories_label = ttk.Label(self.main_frame, text="Total Calories: 0", font=("Helvetica", 14, "bold"), background="#f0f0f0")
        self.total_calories_label.pack(pady=10)
        
        self.delete_button = ttk.Button(self.add_meal_frame, text="Delete", command=self.delete_meal)
        self.delete_button.grid(row=1, column=4, padx=10) 

    def add_meal(self):
        meal = self.meal_entry.get()
        calories = self.calories_entry.get()
        if meal and calories:
            self.meals.append((meal, int(calories)))
            self.update_meals_display()
            self.update_total_calories()
            self.meal_entry.delete(0, tk.END)
            self.calories_entry.delete(0, tk.END)

    def update_meals_display(self):
        self.table.delete(*self.table.get_children())

        for meal, calories in self.meals:
            self.table.insert("", "end", values=(meal, calories))

    def update_total_calories(self):
        self.total_calories = sum(calories for _, calories in self.meals)
        self.total_calories_label.config(text=f"Total Calories: {self.total_calories}")
        
    def delete_meal(self):
        selected_item = self.table.focus()
        if selected_item:
            meal_index = self.table.index(selected_item)
            del self.meals[meal_index]  
            self.table.delete(selected_item)  
            self.update_total_calories() 

root = tk.Tk()
app = CaloFit(root)
root.mainloop()
