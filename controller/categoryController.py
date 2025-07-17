from model.categoryRoutes import CategoryRoutes
from model.category import Category

class CategoryController:
    def __init__(self):
        self.category_routes = CategoryRoutes()

    def get_all_categories(self):
        return self.category_routes.get_all_categories()
    
    def get_category_by_id(self, category_id):
        return self.category_routes.get_category_by_id(category_id)