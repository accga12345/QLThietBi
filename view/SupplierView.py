import tkinter as tk
from tkinter import ttk, messagebox
from controller.supplierController import SupplierController

class SupplierView:
    def __init__(self):
        self.controller = SupplierController()
        self.root = tk.Tk()
        self.root.title("Supplier Management System")

        self.create_widgets()
        self.refresh_suppliers()

    def create_widgets(self):
        tk.Label(self.root, text="Search").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=0, column=1, padx=15, pady=5)
        tk.Button(self.root, text="Search", command=lambda: self.controller.search_supplier(self)).grid(row=0, column=2, padx=5, pady=5)

        # Form nhập dữ liệu bắt đầu từ row=1
        labels = ['Name', 'Contact Person', 'Address', 'Phone', 'Email']
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=idx+1, column=0, padx=5, pady=5, sticky='w')
            entry = tk.Entry(self.root)
            entry.grid(row=idx+1, column=1, padx=5, pady=5)
            self.entries[label.lower().replace(" ", "_")] = entry

        # Buttons (Add, Update, Delete, Refresh)
        tk.Button(self.root, text="Add", command=lambda: self.controller.add_new_supplier(self)).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Update", command=lambda: self.controller.update_supplier(self)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Delete", command=lambda: self.controller.delete_supplier(self)).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Refresh", command=self.refresh_suppliers).grid(row=4, column=2, padx=5, pady=5)

        # Treeview hiển thị danh sách nhà cung cấp
        columns = ('supplier_id', 'name', 'contact_person', 'address', 'phone', 'email')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)

        # Tạo Scrollbar dọc
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào grid
        self.tree.grid(row=len(labels)+2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        scrollbar.grid(row=len(labels)+2, column=3, sticky='ns')

        # Cho phép treeview giãn khi resize window
        self.root.grid_rowconfigure(len(labels)+2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Bind select
        self.tree.bind('<<TreeviewSelect>>', lambda event: self.controller.load_supplier_to_form(self))


    def get_form_data(self):
        data = {}
        for key, entry in self.entries.items():
            value = entry.get()
            data[key] = value
        return data

    def get_selected_supplier_id(self, show_warning=True):
        selected = self.tree.selection()
        if selected:
            return int(self.tree.item(selected[0])['values'][0])
        else:
            if show_warning:
                messagebox.showwarning("Select Supplier", "Please select a supplier first.")
                return None

    def fill_supplier_selected(self, supplier):
        for key, value in supplier.items():
            if key in self.entries:
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, str(value))

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def refresh_suppliers(self):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        suppliers = self.controller.get_all_suppliers()
        for supplier in suppliers:
            self.tree.insert('', tk.END, values=(
                supplier['supplier_id'], supplier['name'], supplier['contact_person'], supplier['address'],
                supplier['phone'], supplier['email']
            ))

    def get_search_term(self):
        return self.search_entry.get()

    def refresh_supplier_list(self, suppliers):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for supplier in suppliers:
            self.tree.insert('', tk.END, values=(
                supplier['supplier_id'], supplier['name'],supplier['contact_person'], supplier['address'],
                supplier['phone'], supplier['email']
            ))

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
