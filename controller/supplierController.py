from model .supplierRoutes import SupplierRoutes
from model.suppiler import Supplier

class SupplierController:
    def __init__(self):
        self.supplierRoutes = SupplierRoutes()
    
    def get_all_suppliers(self):
        return self.supplierRoutes.get_all_suppliers()
    
    def get_name_supplier_by_id(self, supplier_id):
        return self.supplierRoutes.get_name_supplier_by_id(supplier_id)
    
    def add_new_supplier(self, view):
        data = view.get_form_data()
        if not all(data.values()):
            view.show_message("Error", "Please fill in all fields")
            return
        supplier = Supplier(**data)
        if self.supplierRoutes.check_name_exists(supplier.name):
            view.show_message("Error", "Supplier name already exists")
            return
        self.supplierRoutes.add_new_supplier(supplier)
        view.refresh_suppliers()
        view.show_message("Success", "Supplier added successfully")

    def load_supplier_to_form(self, view):
        supplier_id = view.get_selected_supplier_id(show_warning=False)
        if supplier_id:
            supplier = self.supplierRoutes.get_supplier_by_id(supplier_id)
            view.fill_supplier_selected(supplier)
    
    def update_supplier(self, view):
        supplier_id = view.get_selected_supplier_id()
        if not supplier_id:
            view.show_message("Error", "Please select a supplier to update")
            return
        data = view.get_form_data()
        if not all(data.values()):
            view.show_message("Error", "Please fill in all fields")
            return
        supplier = Supplier(**data)
        if self.supplierRoutes.check_name_exists(supplier.name):
            view.show_message("Error", "Supplier name already exists")
            return
        self.supplierRoutes.update_supplier(supplier_id, supplier)
        view.refresh_suppliers()
        view.show_message("Success", "Supplier updated successfully")

    def delete_supplier(self, view):
        supplier_id = view.get_selected_supplier_id()
        if supplier_id:
            self.supplierRoutes.delete_supplier(supplier_id)
            view.refresh_suppliers()
            view.show_message("Success", "Supplier deleted successfully")
        else:
            view.show_message("Error", "Please select a supplier to delete")

    def show_devices_by_supplier_id(self, view):
        supplier_id = view.get_supplier_id()
        devices = self.supplierRoutes.get_devices_by_supplier_id(supplier_id)
        view.refresh_device_list(devices)
    
    