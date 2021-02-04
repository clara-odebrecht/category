from src.dao.base_dao import BaseDao
from src.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseDao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)

    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        if result:
            return result
        else:
            raise Exception('Object not found into database.')

    def read_all(self) -> list:
        list = self.__dao.read_all()
        return list

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
