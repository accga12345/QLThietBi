import tkinter as tk
from tkinter import ttk, messagebox
from controller.deviceController import DeviceController


class DeviceView:
    def __init__(self):
        self.controller = DeviceController()
        self.root = tk.Tk()
        self.root.title("Device Management System")

        self.create_widgets()
        self.refresh_devices()


    def create_widgets(self):
        tk.Label(self.root, text="Search").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=0, column=1, padx=15, pady=5)
        tk.Button(self.root, text="Search", command=lambda: self.controller.search_device(self)).grid(row=0, column=2, padx=5, pady=5)

        # Form nhập dữ liệu bắt đầu từ row=1
        labels = ['Name', 'Category', 'Supplier', 'Quantity', 'Price', 'Manufacturer', 'Description', 'Status']
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=idx+1, column=0, padx=5, pady=5, sticky='w')

            if label == 'Category':
                categories = self.controller.get_all_categories()
                self.category_name_to_id = {category['name']: category['category_id'] for category in categories}
                combo = ttk.Combobox(self.root, values=list(self.category_name_to_id.keys()))
                combo.grid(row=idx+1, column=1, padx=5, pady=5)
                self.entries['category_id'] = combo

            elif label == 'Supplier':
                suppliers = self.controller.get_all_suppliers()
                self.supplier_name_to_id = {supplier['name']: supplier['supplier_id'] for supplier in suppliers}
                combo = ttk.Combobox(self.root, values=list(self.supplier_name_to_id.keys()))
                combo.grid(row=idx+1, column=1, padx=5, pady=5)
                self.entries['supplier_id'] = combo

            else:
                entry = tk.Entry(self.root)
                entry.grid(row=idx+1, column=1, padx=5, pady=5)
                self.entries[label.lower().replace(" ", "_")] = entry

        # Buttons (Add, Update, Delete, Refresh) đặt tiếp theo
        tk.Button(self.root, text="Add", command=lambda: self.controller.add_device(self)).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Update", command=lambda: self.controller.update_device(self)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Delete", command=lambda: self.controller.delete_device(self)).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Refresh", command=self.refresh_devices).grid(row=4, column=2, padx=5, pady=5)

        # Treeview hiển thị danh sách thiết bị đặt dưới cùng
        columns = ('device_id', 'name', 'category', 'supplier', 'quantity', 'price', 'manufacturer', 'description', 'status')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
            
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào grid
        self.tree.grid(row=len(labels)+2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        scrollbar.grid(row=len(labels)+2, column=3, sticky='ns')

        # Cho phép treeview giãn khi resize window
        self.root.grid_rowconfigure(len(labels)+2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.tree.bind('<<TreeviewSelect>>', lambda event: self.controller.load_device_to_form(self))



    def get_form_data(self):
        data = {}
        for key, entry in self.entries.items():
            value = entry.get()
            if key == 'category_id':
                value = self.category_name_to_id.get(value, 0)
            if key == 'supplier_id':
                value = self.supplier_name_to_id.get(value, 0)
            if key == 'quantity':
                value = int(value) if value else 0
            if key == 'price':
                value = float(value) if value else 0.0
            data[key] = value
        return data

    def get_selected_device_id(self, show_warning=True):
        selected = self.tree.selection()
        if selected:
            return int(self.tree.item(selected[0])['values'][0])
        else:
            if show_warning:
                messagebox.showwarning("Select Device", "Please select a device first.")
                return None
    
    def fill_device_selected(self, device):
        for key, value in device.items():
            if key in self.entries:
                entry = self.entries[key]

                if key == 'category_id':
                    # Lấy name từ id
                    for name, id_ in self.category_name_to_id.items():
                        if id_ == value:
                            entry.set(name)  # set combobox value
                            break

                elif key == 'supplier_id':
                    for name, id_ in self.supplier_name_to_id.items():
                        if id_ == value:
                            entry.set(name)
                            break

                else:
                    entry.delete(0, tk.END)
                    entry.insert(0, str(value))

    
    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def refresh_devices(self):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        devices = self.controller.get_all_devices()
        for device in devices:
            self.tree.insert('', tk.END, values=(
                device['device_id'], device['name'], self.controller.get_category_by_id(device['category_id']),
                self.controller.get_name_supplier_by_id(device['supplier_id']),
                device['quantity'], device['price'], device['manufacturer'],
                device['description'], device['status']
            ))

    def get_search_term(self):
        return self.search_entry.get()
        
    def refresh_device_list(self, devices):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for device in devices:
            self.tree.insert('', tk.END, values=(
                device['device_id'], device['name'], self.controller.get_category_by_id(device['category_id']),
                self.controller.get_name_supplier_by_id(device['supplier_id']),
                device['quantity'], device['price'], device['manufacturer'],
                device['description'], device['status']
            ))

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
