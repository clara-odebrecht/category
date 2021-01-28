from src.models.category import Category

from unittest import TestCase

class TryTesting(TestCase):
    _category = Category('Eltrônicos')

    def test_model_instance(self):
        assert isinstance(self._category, Category)

    def test_attr_values(self):
        assert self._category.name == 'Eltrônicos'
        assert self._category.description == None
        assert self._category.identifier == None

    def test_attr_types(self):
        assert isinstance(self._category.name, str)
        assert isinstance(self._category.description, None)
        assert isinstance(self._category.identifier, None)