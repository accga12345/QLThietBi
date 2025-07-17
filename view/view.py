import tkinter as tk
from tkinter import ttk, messagebox


class DeviceView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Device Management System")

        self.create_widgets()
        self.refresh_devices()


    def create_widgets(self):
        tk.Label(self.root, text="Search").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=0, column=1, padx=15, pady=5)
        tk.Button(self.root, text="Search", command=self.controller.search_device).grid(row=0, column=2, padx=5, pady=5)

        # Form nhập dữ liệu bắt đầu từ row=1
        labels = ['Name', 'Category', 'Quantity', 'Price', 'Manufacturer', 'Description', 'Status']
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=idx+1, column=0, padx=5, pady=5, sticky='w')

            if label == 'Category':
                categories = self.controller.get_all_categories()
                self.category_name_to_id = {category['name']: category['category_id'] for category in categories}
            
                combo = ttk.Combobox(self.root, values=list(self.category_name_to_id.keys()))
                combo.grid(row=idx+1, column=1, padx=5, pady=5)
                self.entries['category_id'] = combo
            else:
                entry = tk.Entry(self.root)
                entry.grid(row=idx+1, column=1, padx=5, pady=5)
                self.entries[label.lower().replace(" ", "_")] = entry

        # Buttons (Add, Update, Delete, Refresh) đặt tiếp theo
        tk.Button(self.root, text="Add", command=self.controller.add_device).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Update", command=self.controller.update_device).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Delete", command=self.controller.delete_device).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Refresh", command=self.refresh_devices).grid(row=4, column=2, padx=5, pady=5)

        # Treeview hiển thị danh sách thiết bị đặt dưới cùng
        columns = ('device_id', 'name', 'category', 'quantity', 'price', 'manufacturer', 'description', 'status')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.grid(row=len(labels)+2, column=0, columnspan=3, padx=5, pady=5)
        self.tree.bind('<<TreeviewSelect>>', lambda event: self.controller.load_device_to_form())



    def get_form_data(self):
        data = {}
        for key, entry in self.entries.items():
            value = entry.get()
            if key in ['category_id']:
                value = self.category_name_to_id.get(value,0)
            if key in ['quantity']:
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
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, str(value))
    
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
                device['quantity'], device['price'], device['manufacturer'],
                device['description'], device['status']
            ))

    def get_search_term(self):
        return self.search_entry.get()
        
    def refresh_device_list(self, device):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for device in device:
            self.tree.insert('', tk.END, values=(
                device['device_id'], device['name'], self.controller.get_category_by_id(device['category_id']),
                device['quantity'], device['price'], device['manufacturer'],
                device['description'], device['status']
            ))

    def show_message(self, title, message):
        
        messagebox.showinfo(title, message)
