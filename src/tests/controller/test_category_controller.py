import sys
sys.path.append('.')

from src.controllers.base_controller import BaseController
from src.controllers.category_controller import CategoryController
import pytest


@pytest.fixture
def create_instance():
    categories = CategoryController()
    return categories


def test_category_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)
    

def test_read_by_id_with_invalid_id_should_raise_exception(create_instance):
    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(3123213156)
    assert str(exc.value) == "Object not found into database."
