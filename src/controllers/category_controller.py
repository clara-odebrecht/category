from src.dao.category_dao import CategoryDao
from src.controllers.base_controller import BaseController


class CategoryController(BaseController):
    def __init__(self) -> None:
        self.__dao = CategoryDao()
        super().__init__(self.__dao)
