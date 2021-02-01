import sys
sys.path.append('.')

from src.models.category import Category
from unittest import TestCase
import pytest


class TryTesting(TestCase):        
    def test_name_none(self):
        with pytest.raises(TypeError):
            c = Category(None, 'Bebida')
        
    def test_name_empty(self):
        with pytest.raises(ValueError):
            c = Category('', 'Bebida')
        
    def test_name_len(self):
        with pytest.raises(ValueError):
            c = Category('Bebida' * 100, 'Nacional')     
            
    def test_name_type(self):
        with pytest.raises(TypeError):
            c = Category(100, 'Nacional')                   
            
    def test_description_type(self):
        with pytest.raises(TypeError):
            c = Category('Bebida', 10.6)       
            
    def test_description_len(self):
        with pytest.raises(ValueError):
            c = Category('Bebida', 'Nacional' * 255)      