from connect_db import connect_db


class CategoryRoutes:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor(dictionary=True)
    
    def get_all_categories(self):
        query = "SELECT  * FROM category"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def get_category_by_id(self, category_id):
        query = "SELECT * FROM category WHERE category_id = %s"
        self.cursor.execute(query, (category_id,))
        result = self.cursor.fetchone()
        return result