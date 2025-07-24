from model.deviceRoutes import DeviceRoutes
from model.device import Device
from controller.categoryController import CategoryController
from controller.supplierController import SupplierController

class DeviceController:
    def __init__(self):
        self.device_routes = DeviceRoutes()
        self.category_controller = CategoryController()
        self.supplier_controller = SupplierController()


    def get_all_devices(self):
        return self.device_routes.get_all_devices()
    
    def get_all_categories(self):
        return self.category_controller.get_all_categories()
    
    def get_all_suppliers(self):
        return self.supplier_controller.get_all_suppliers()
    
    def get_category_by_id(self, category_id):
        categories = self.category_controller.get_all_categories()
        for category in categories:
            if category['category_id'] == category_id:
                return category['name']
        return None
    
    def get_name_supplier_by_id(self, supplier_id):
        suppliers = self.supplier_controller.get_all_suppliers()
        for supplier in suppliers:
            if supplier['supplier_id'] == supplier_id:
                return supplier['name']
        return None
    
    def add_device(self, view):
        data = view.get_form_data()
        # kiểm tra điền đầy đủ thông tin chưa
        if not all(data.values()):
            view.show_message("Error", "Please fill in all fields")
            return
        device = Device(**data)
        if self.device_routes.check_name_exists(device.name):
            view.show_message("Error", "Device name already exists")
            return
        self.device_routes.add_device(device)
        view.refresh_devices()
        view.show_message("Success", "Device added successfully")
        
    def update_device(self, view):
        device_id = view.get_selected_device_id()
        if not device_id:
            view.show_message("Error", "Please select a device to update")
            return
        data = view.get_form_data()
        if not all(data.values()):
            view.show_message("Error", "Please fill in all fields")
            return
        device = Device(**data)
        device.device_id = device_id

        if self.device_routes.check_name_exists(device.name, device_id):
            view.show_message("Error", "Device name already exists")
            return

        self.device_routes.update_device(device_id, device)
        view.refresh_devices()
        view.show_message("Success", "Device updated successfully")

    def delete_device(self, view):
        device_id = view.get_selected_device_id()
        if device_id:
            self.device_routes.delete_device(device_id)
            view.refresh_devices()
            view.show_message("Success", "Device deleted successfully")
        else:
            view.show_message("Error", "Please select a device to delete")

    def search_device(self, view):
        search_term = view.get_search_term()
        devices = self.device_routes.search_devices(search_term)
        view.refresh_device_list(devices)

    def load_device_to_form(self, view):
        device_id = view.get_selected_device_id(show_warning=False)
        if device_id:
            device = self.device_routes.get_device_by_id(device_id)
            if device:
                view.fill_device_selected(device)
            
    def import_quantity(self, view):
        device_id = view.get_selected_device_id(show_warning=False)
        if device_id:
            quantity = view.get_quantity()
            self.device_routes.import_quantity(device_id, quantity)
            view.refresh_devices()
            view.show_message("Success", "Quantity imported successfully")

    def export_quantity(self, view):
        device_id = view.get_selected_device_id(show_warning=False)
        if device_id:
            quantity = view.get_quantity()
            device = self.device_routes.get_device_by_id(device_id)
            remaining_quantity = device['quantity'] - quantity
            if remaining_quantity < 0:
                view.show_message("Error", "Vui lòng nhập số lượng phù hợp để xuất hàng")
                return
            elif remaining_quantity == 0:
                self.device_routes.export_quantity(device_id, quantity)
                self.device_routes.delete_device(device_id)
                view.refresh_devices()
                view.show_message("Success", "Thiết bị đã hết hàng và đã bị xóa")
            else:
                self.device_routes.export_quantity(device_id, quantity)
                view.refresh_devices()
                view.show_message("Success", "Quantity exported successfully")

    
    def search_device_import_export(self, view):
        search_term = view.get_search_term()
        devices = self.device_routes.search_devices(search_term)
        view.refresh_device_list(devices)

    def load_device_to_form_import_export(self, view):
        device_id = view.get_selected_device_id(show_warning=False)
        if device_id:
            device = self.device_routes.get_device_by_id(device_id)
            if device:
                view.fill_device_selected(device)

    def get_device_by_supplier_id(self, view):
        supplier_id = view.get_supplier_id()
        devices = self.device_routes.get_devices_by_supplier_id(supplier_id)
        view.refresh_device_list(devices)
         