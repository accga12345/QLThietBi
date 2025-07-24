from connect_db import connect_db

class DeviceRoutes:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor(dictionary=True)
    
    def get_all_devices(self):
        query = "SELECT  * FROM device"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def  get_device_by_id(self, device_id):
        query = "SELECT * FROM device WHERE device_id = %s"
        self.cursor.execute(query, (device_id,))
        result = self.cursor.fetchone()
        return result

    def add_device(self, device):
        query = "INSERT INTO device (name, category_id, quantity, price, manufacturer, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (
            device.name,
            device.category_id,
            device.quantity,
            device.price,
            device.manufacturer,
            device.description,
            device.status
        ))
        self.conn.commit()

    def update_device(self, device_id, device):
        query = "UPDATE device SET name = %s, category_id = %s, quantity = %s, price = %s, manufacturer = %s, description = %s, status = %s WHERE device_id = %s"
        self.cursor.execute(query, (
            device.name,
            device.category_id,
            device.quantity,
            device.price,
            device.manufacturer,
            device.description,
            device.status,
            device_id
        ))
        self.conn.commit()
    
    def delete_device(self,device_id):
        query = "DELETE FROM device WHERE device_id = %s"
        self.cursor.execute(query,(device_id,))
        self.conn.commit()
    
    def check_name_exists(self, name, exclude_id=None):
        if exclude_id is not None:
            query = "SELECT * FROM supplier WHERE name = %s AND supplier_id != %s"
            self.cursor.execute(query, (name, exclude_id))
        else:
            query = "SELECT * FROM supplier WHERE name = %s"
            self.cursor.execute(query, (name,))
        result = self.cursor.fetchone()
        return result


    def search_devices(self, query):
        self.cursor.execute("SELECT * FROM device WHERE name LIKE %s", ('%' + query + '%',))
        result = self.cursor.fetchall()
        return result

    def import_quantity(self, device_id, quantity):
        query = "UPDATE device SET quantity = quantity + %s WHERE device_id = %s"
        self.cursor.execute(query, (quantity, device_id))
        self.conn.commit()

    def export_quantity(self, device_id, quantity):
        query = "UPDATE device SET quantity = quantity - %s WHERE device_id = %s"
        self.cursor.execute(query, (quantity, device_id))
        self.conn.commit()

    def get_devices_by_supplier_id(self, supplier_id):
        query = "SELECT * FROM device WHERE supplier_id = %s"
        self.cursor.execute(query, (supplier_id,))
        result = self.cursor.fetchall()
        return result
