from connect_db import connect_db

class SupplierRoutes:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all_suppliers(self):
        query = "SELECT  * FROM supplier"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def get_supplier_by_id(self, supplier_id):
        query = "SELECT * FROM supplier WHERE supplier_id = %s"
        self.cursor.execute(query, (supplier_id,))
        result = self.cursor.fetchone()
        return result

    def get_name_supplier_by_id(self, supplier_id):
        query = "SELECT name FROM supplier WHERE supplier_id = %s"
        self.cursor.execute(query, (supplier_id,))
        result = self.cursor.fetchone()
        return result
    def add_new_supplier(self, supplier):
        query = "INSERT INTO supplier (name, contact_person, phone, email, address) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (supplier.name, supplier.contact_person, supplier.phone, supplier.email, supplier.address))
        self.conn.commit()

    def update_supplier(self, supplier_id, supplier):
        query = "UPDATE supplier SET name = %s, contact_person = %s, phone = %s, email = %s, address = %s WHERE supplier_id = %s"
        self.cursor.execute(query, (supplier.name, supplier.contact_person, supplier.phone, supplier.email, supplier.address, supplier_id))
        self.conn.commit()

    def delete_supplier(self, supplier_id):
        query = "DELETE FROM supplier WHERE supplier_id = %s"
        self.cursor.execute(query, (supplier_id,))
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
    
    def search_suppliers(self, query):
        self.cursor.execute("SELECT * FROM supplier WHERE name LIKE %s", ('%' + query + '%',))
        result = self.cursor.fetchall()
        return result
