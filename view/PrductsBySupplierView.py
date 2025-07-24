import tkinter as tk
from tkinter import ttk, messagebox
from controller.deviceController import DeviceController

class ProductsBySupplierView:
    def __init__(self):
        self.controller = DeviceController()
        self.root = tk.Tk()
        self.root.title("Products By Supplier")

        self.create_widgets()
        self.refresh_devices()

    def create_widgets(self):
        tk.Label(self.root, text="Chọn nhà cung cấp:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Combobox chọn nhà cung cấp (giống DeviceView)
        suppliers = self.controller.get_all_suppliers()
        self.supplier_name_to_id = {supplier['name']: supplier['supplier_id'] for supplier in suppliers}
        self.supplier_combo = ttk.Combobox(self.root, values=list(self.supplier_name_to_id.keys()), state='readonly', width=30)
        self.supplier_combo.grid(row=0, column=1, padx=10, pady=10)

        # Nút Xem sản phẩm
        tk.Button(self.root, text="Xem sản phẩm",command=lambda: self.controller.get_device_by_supplier_id(self)).grid(row=0, column=2, padx=10, pady=10)

        # Nút Refresh
        tk.Button(self.root, text="Refresh", command=self.refresh_devices).grid(row=0, column=3, padx=10, pady=10)

        # Treeview hiển thị thiết bị
        columns = ('device_id', 'name', 'category', 'supplier', 'quantity', 'price', 'manufacturer', 'description', 'status')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Scrollbar dọc
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=4, sticky='ns')

        # Cho phép giãn Treeview khi resize window
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


    def refresh_devices(self):
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

    def get_supplier_id(self):
        supplier_name = self.supplier_combo.get()
        return self.supplier_name_to_id.get(supplier_name)
    
    def refresh_device_list(self, devices):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for device in devices:
            self.tree.insert('', tk.END, values=(
                device['device_id'], device['name'], self.controller.get_category_by_id(device['category_id']),
                self.controller.get_name_supplier_by_id(device['supplier_id']),
                device['quantity'], device['price'], device['manufacturer'],
                device['description'], device['status']
            ))
    
    
