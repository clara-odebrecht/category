import sys
sys.path.append('.')

from src.dao.category_dao import CategoryDao
from src.models.category import Category
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest

class TestCategoryDao:
    dao = CategoryDao()

    @pytest.fixture
    def create_instance(self):
        categories = Category("Mobile", "Wearable Device")
        return categories

    def test_instance(self):
        assert isinstance(self.dao, CategoryDao)

    def test_save(self, create_instance):
        categories_saved = self.dao.save(create_instance)
        assert categories_saved.id is not None
        self.dao.delete(categories_saved)

    def test_read_by_id(self, create_instance):
        categories_saved = self.dao.save(create_instance)
        categories_read = self.dao.read_by_id(categories_saved.id)
        assert isinstance(categories_read, Category)
        self.dao.delete(categories_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            self.dao.read_by_id('id')

    def test_read_all(self):
        result = self.dao.read_all()
        assert isinstance(result, list)

    def test_delete(self, create_instance):
        categories_saved = self.dao.save(create_instance)
        categories_read = self.dao.read_by_id(categories_saved.id)
        self.dao.delete(categories_read)
        categories_read = self.dao.read_by_id(categories_saved.id)
        assert categories_read is None

    def test_not_saved(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.save("Cellphone")

    def test_not_deleted(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.delete("Categories")
