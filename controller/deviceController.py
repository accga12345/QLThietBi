from model.deviceRoutes import DeviceRoutes
from model.device import Device
from controller.categoryController import CategoryController

class DeviceController:
    def __init__(self):
        self.view = None
        self.device_routes = DeviceRoutes()
        self.category_controller = CategoryController()
        

    def get_all_devices(self):
        return self.device_routes.get_all_devices()
    
    def get_all_categories(self):
        return self.category_controller.get_all_categories()
    
    def get_category_by_id(self, category_id):
        categories = self.category_controller.get_all_categories()
        for category in categories:
            if category['category_id'] == category_id:
                return category['name']
        return None
    
    def add_device(self):
        data = self.view.get_form_data()
        device = Device(**data)
        if self.device_routes.check_name_exists(device.name):
            self.view.show_message("Error", "Device name already exists")
            return
        self.device_routes.add_device(device)
        self.view.refresh_devices()
        self.view.show_message("Success", "Device added successfully")
        

    def update_device(self):
        device_id = self.view.get_selected_device_id()
        if not device_id:
            self.view.show_message("Error", "Please select a device to update")
            return
        data = self.view.get_form_data()
        device = Device(**data)
        device.device_id = device_id

        if self.device_routes.check_name_exists(device.name):
            self.view.show_message("Error", "Device name already exists")
            return

        self.device_routes.update_device(device_id, device)
        self.view.refresh_devices()
        self.view.show_message("Success", "Device updated successfully")

    def delete_device(self):
        device_id = self.view.get_selected_device_id()
        if device_id:
            self.device_routes.delete_device(device_id)
            self.view.refresh_device()
            self.view.show_message("Success", "Device deleted successfully")
        else:
            self.view.show_message("Error", "Please select a device to delete")

    def search_device(self):
        search_term = self.view.get_search_term()
        devices = self.device_routes.search_devices(search_term)
        self.view.refresh_device_list(devices)

    def load_device_to_form(self):
        device_id = self.view.get_selected_device_id(show_warning=False)
        if device_id:
            device = self.device_routes.get_device_by_id(device_id)
            if device:
                self.view.fill_device_selected(device)
            
        
    def set_view(self, view):
        self.view = view


    
    
