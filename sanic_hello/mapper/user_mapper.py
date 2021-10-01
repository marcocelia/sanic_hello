from typing import List

from sanic_hello.dto.user_dto import UserDTO
from sanic_hello.model.user_model import User


def to_dto(user: User) -> UserDTO:
    user_dict = user.to_mongo().to_dict()
    user_dict['_id'] = str(user.id)
    return UserDTO().load(user_dict)


def to_dto_list(users: List[User]) -> List[UserDTO]:
    return list(map(lambda user: to_dto(user), users))
