import tkinter as tk
from view.ManageProductsView import DeviceView
from view.ManageImportAndExport import ImportAndExport
from view.SupplierView import SupplierView
from view.PrductsBySupplierView import ProductsBySupplierView


class HomeView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Device Management System")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Home", font=('Arial', 16)).grid(row=0, column=0, columnspan=2, pady=20)

        # Nút Nhập/Xuất
        tk.Button(self.root, text="Nhập/Xuất", width=20, command=self.open_import_export).grid(row=1, column=0, padx=10, pady=10)

        # Nút Quản lý sản phẩm
        tk.Button(self.root, text="Quản lý sản phẩm", width=20, command=self.open_manage_products).grid(row=2, column=0, padx=10, pady=10)

        # Nút Quản lý nhà cung cấp
        tk.Button(self.root, text="Quản lý nhà cung cấp", width=20, command=self.open_manage_suppliers).grid(row=3, column=0, padx=10, pady=10)

        # Nút xem sản phẩm được cung cấp
        tk.Button(self.root, text="Danh mục sản phẩm theo nhà cung cấp", width=40, command=self.open_manage_products_by_supplier).grid(row=4, column=0, padx=10, pady=10)

    def open_import_export(self):
        ImportAndExport()

    def open_manage_products(self):
        DeviceView()

    def open_manage_suppliers(self):
        SupplierView()

    def open_manage_products_by_supplier(self):
        ProductsBySupplierView()