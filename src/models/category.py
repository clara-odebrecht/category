from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

class Category:
    __tablename__ = 'category'

    identifier = Column('id', Integer, primary_key=True)
    name = Column('name', String(length=50), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, description: str == None,
                identifier: int == None) -> None:
        self.name = name
        self.description = description
        self.identifier = identifier

    @validates('name')
    def validate_name(self, key, name):
        if isinstance(name, str) == False:
            raise ValueError('Please, write a valid type name.')
        elif name.replace(" ", "") == "":
            raise ValueError('Please, write a name.')
        elif name.length > 50:
            raise ValueError('The max lenght is 50 characters.')
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if (isinstance(description, str) == False) or (isinstance(description, None) == False):
            raise ValueError('Please, write a valid type description.')
        elif (isinstance(description, str) == True) and (description.replace(" ", "") == ""):
            raise ValueError('Please, write a description.')
        elif (isinstance(description, str) == True) and (description.length > 50):
            raise ValueError('The max lenght is 50 characters.')
        return description