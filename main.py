import tkinter as tk
from tkinter import messagebox, ttk

class EmployeeManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x600")  
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(True, True)

        self.main_frame = tk.Frame(self.root, bg="#f8f9fa")
        self.main_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=780, height=580)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.main_frame, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.content_frame = tk.Frame(self.canvas, bg="#f8f9fa")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor='nw')

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12), rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))

        title_label = tk.Label(self.content_frame, text="Employee Management System", font=("Arial", 20, "bold"), bg="#007bff", fg="white", padx=10, pady=10)
        title_label.pack(fill="x")

        frame = tk.Frame(self.content_frame, bg="#ffffff", padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        frame.pack(pady=10, fill="x", padx=10)

        entry_name = tk.Entry(frame, width=25, font=("Arial", 12))
        entry_name.grid(row=0, column=0, padx=5, pady=5)
        
        spin_age = tk.Spinbox(frame, from_=18, to=100, font=("Arial", 12), width=5)
        spin_age.grid(row=0, column=1, padx=5, pady=5)
        
        entry_department = tk.Entry(frame, width=25, font=("Arial", 12))
        entry_department.grid(row=0, column=2, padx=5, pady=5)

        btn_frame = tk.Frame(self.content_frame, bg="#ffffff", padx=10, pady=10)
        btn_frame.pack(fill="x", padx=20)

        add_button = tk.Button(btn_frame, text="Add Employee", command=lambda: self.add_employee(entry_name, spin_age, entry_department), bg="#28a745", fg="white", font=("Arial", 12), width=15, relief=tk.RAISED, bd=3)
        add_button.grid(row=0, column=0, padx=5, pady=5)
        update_button = tk.Button(btn_frame, text="Update Employee", command=self.update_employee, bg="#ffc107", fg="black", font=("Arial", 12), width=15, relief=tk.RAISED, bd=3)
        update_button.grid(row=0, column=1, padx=5, pady=5)
        delete_button = tk.Button(btn_frame, text="Delete Employee", command=self.delete_employee, bg="#dc3545", fg="white", font=("Arial", 12), width=15, relief=tk.RAISED, bd=3)
        delete_button.grid(row=0, column=2, padx=10, pady=5)

        search_frame = tk.Frame(self.content_frame, bg="#ffffff", padx=10, pady=10)
        search_frame.pack(fill="x", padx=20)
        entry_search = tk.Entry(search_frame, width=40, font=("Arial", 12))
        entry_search.pack(side="left", padx=10)
        search_button = tk.Button(search_frame, text="Search Employee", command=lambda: self.search_employee(entry_search), bg="#17a2b8", fg="white", font=("Arial", 12), relief=tk.RAISED, bd=3)
        search_button.pack(side="left", padx=10)

        table_frame = tk.Frame(self.content_frame, bg="#ffffff", padx=20, pady=10)
        table_frame.pack(fill="both", expand=True, padx=20)
        columns = ("Name", "Age", "Department")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("Department", text="Department")
        self.table.pack(fill="both", expand=True)

        table_frame.config(relief=tk.RIDGE, borderwidth=2)
        frame.config(relief=tk.RIDGE, borderwidth=2)
        btn_frame.config(relief=tk.RIDGE, borderwidth=2)
        search_frame.config(relief=tk.RIDGE, borderwidth=2)

        self.tab_control = ttk.Notebook(self.content_frame)
        self.tab_control.pack(expand=1, fill="both")

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Employee Profile")

        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Time-Off Management")

        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text="Performance Management")


        self.create_employee_profile_tab()
        self.create_time_off_management_tab()
        self.create_performance_management_tab()

        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_employee_profile_tab(self):
        self.name_label = tk.Label(self.tab1, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.tab1)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.tab1, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.tab1)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.tab1, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.tab1)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self.tab1, text="Save", command=self.save_employee_profile)
        self.save_button.grid(row=3, column=1, padx=5, pady=5)


    def create_time_off_management_tab(self):
        # Create labels and entries
        self.start_date_label = tk.Label(self.tab2, text="Start Date:")
        self.start_date_label.grid(row=0, column=0)
        self.start_date_entry = tk.Entry(self.tab2)
        self.start_date_entry.grid(row=0, column=1)

        self.end_date_label = tk.Label(self.tab2, text="End Date:")
        self.end_date_label.grid(row=1, column=0)
        self.end_date_entry = tk.Entry(self.tab2)
        self.end_date_entry.grid(row=1, column=1)

        # Create button
        self.request_time_off_button = tk.Button(self.tab2, text="Request Time Off", command=self.request_time_off)
        self.request_time_off_button.grid(row=2, column=1)

    def create_performance_management_tab(self):
        # Create labels and entries
        self.goal_label = tk.Label(self.tab3, text="Goal:")
        self.goal_label.grid(row=0, column=0)
        self.goal_entry = tk.Entry(self.tab3)
        self.goal_entry.grid(row=0, column=1)

        self.progress_label = tk.Label(self.tab3, text="Progress:")
        self.progress_label.grid(row=1, column=0)
        self.progress_entry = tk.Entry(self.tab3)
        self.progress_entry.grid(row=1, column=1)


        self.save_progress_button = tk.Button(self.tab3, text="Save Progress", command=self.save_progress)
        self.save_progress_button.grid(row=2, column=1)

    def add_employee(self, entry_name, spin_age, entry_department):
        name = entry_name.get()
        age = spin_age.get()
        department = entry_department.get()
        if name and department:
            self.table.insert("", "end", values=(name, age, department))
            entry_name.delete(0, tk.END)
            entry_department.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Name and Department cannot be empty!")

    def update_employee(self):
        selected_item = self.table.selection()
        if selected_item:
            # Update employee details here
            pass
        else:
            messagebox.showwarning("Selection Error", "Please select an employee to update!")

    def delete_employee(self):
        selected_item = self.table.selection()
        if selected_item:
            self.table.delete(selected_item)
        else:
            messagebox.showwarning("Selection Error", "Please select an employee to delete!")

    def search_employee(self, entry_search):
        search_term = entry_search.get().lower()
        for row in self.table.get_children():
            values = self.table.item(row)['values']
            if search_term in str(values).lower():
                self.table.selection_set(row)
                return
        messagebox.showinfo("Search", "Employee not found!")

    def save_employee_profile(self):
        # Save employee profile to database
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

       
       

        messagebox.showinfo("Success", "Employee profile saved successfully")

    def request_time_off(self):
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

      

        messagebox.showinfo("Success", "Time off request submitted successfully")

    def save_progress(self):
      
        goal = self.goal_entry.get()
        progress = self.progress_entry.get()


        messagebox.showinfo("Success", "Progress saved successfully")


if _name_ == "_main_":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()


Added main.py - initial code for Employee Management System
