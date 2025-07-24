import tkinter as tk
from tkinter import ttk, messagebox
from controller.deviceController import DeviceController
from view.ManageProductsView import DeviceView

class ImportAndExport(DeviceView):
    def __init__(self):
        self.controller = DeviceController()
        self.root = tk.Tk()
        self.root.title("Manage_Import_Export")

        self.create_widgets()
        self.refresh_devices()

    def create_widgets(self):
        tk.Label(self.root, text="Search").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=0, column=1, padx=15, pady=5)
        tk.Button(self.root, text="Search", command=lambda:self.controller.search_device_import_export(self)).grid(row=0, column=2, padx=5, pady=5)

        # Form
        labels = ['Name','Quantity']
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=idx+1, column=0, padx=5, pady=5, sticky='w')
            entry = tk.Entry(self.root)
            entry.grid(row=idx+1, column=1, padx=5, pady=5)
            self.entries[label.lower().replace(" ", "_")] = entry

        tk.Button(self.root, text="Import", command=lambda:self.controller.import_quantity(self)).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Export", command=lambda:self.controller.export_quantity(self)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.root, text="Refresh", command=lambda:self.refresh_devices).grid(row=3, column=2, padx=5, pady=5)

        # Treeview hiển thị danh sách thiết bị
        columns = ('device_id', 'name', 'quantity')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.grid(row=len(labels)+2, column=0, columnspan=3, padx=5, pady=5)
        self.tree.bind('<<TreeviewSelect>>', lambda event: self.controller.load_device_to_form_import_export(self))

    
    def refresh_devices(self):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        devices = self.controller.get_all_devices()
        for device in devices:
            self.tree.insert('', tk.END, values=(device['device_id'], device['name'], device['quantity']))

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def get_selected_device_id(self, show_warning=True):
        selected = self.tree.selection()
        if selected:
            return int(self.tree.item(selected[0])['values'][0])
        else:
            if show_warning:
                messagebox.showwarning("Select Device", "Please select a device first.")
            return None
    
    def fill_device_selected(self, device):
        self.entries['name'].delete(0, tk.END)  
        self.entries['name'].insert(0, device['name'])

    
    def get_quantity(self):
        return int(self.entries['quantity'].get())
    
    def get_search_term(self):
        return self.search_entry.get()

    def refresh_device_list(self, device):
        self.clear_entries()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for device in device:
            self.tree.insert('', tk.END, values=(device['device_id'], device['name'], device['quantity']))

    
    

