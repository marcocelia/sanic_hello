from functools import wraps

from marshmallow import ValidationError
from sanic import Request
from sanic.exceptions import SanicException


def dto_validator(schema):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request: Request, *args, **kwargs):
            try:
                dto: schema = schema().load(request.json)
                response = await f(request, *args, dto=dto, **kwargs)
                return response
            except ValidationError as err:
                raise SanicException(message=err.messages, status_code=400)
        return decorated_function
    return decorator
