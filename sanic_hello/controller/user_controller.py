from sanic import Blueprint
from sanic.exceptions import NotFound
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, json

from sanic_hello.dto.user_dto import UserCreateDTO, UserUpdateDTO
from sanic_hello.mapper import user_mapper
from sanic_hello.model.user_model import User
from sanic_hello.core.validator.validate_request import dto_validator

bp = Blueprint(name="users", url_prefix="/users", strict_slashes=True)


@bp.get("/")
async def get_all(request: Request) -> HTTPResponse:
    return json(user_mapper.to_dto_list(User.objects.scalar()), status=200)


@bp.get("/<user_id>")
async def get_one(request: Request, user_id) -> HTTPResponse:
    logger.info(user_id)
    user = User.objects.get(id=user_id)
    if not user:
        raise NotFound(user_id)
    return json(user_mapper.to_dto(user), status=200)


@bp.post("/")
@dto_validator(UserCreateDTO)
async def create(request: Request, dto: UserCreateDTO) -> HTTPResponse:
    model = User(name=dto['name'], email=dto['email'])
    model.save()
    return json(user_mapper.to_dto(model), status=201)


@bp.put("/<user_id>")
@dto_validator(UserUpdateDTO)
async def update(request: Request, user_id, dto: UserUpdateDTO) -> HTTPResponse:
    return json(dto)


@bp.delete("/<user_id>")
async def delete(request: Request, user_id) -> HTTPResponse:
    logger.info(user_id)
    user = User.objects.get(id=user_id)
    if not user:
        raise NotFound(user_id)
    return json(user_mapper.to_dto(user), status=200)
