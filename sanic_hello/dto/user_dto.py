from marshmallow import Schema, fields


class UserCreateDTO(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime()


class UserDTO(UserCreateDTO):
    _id = fields.Str(required=True)


class UserUpdateDTO(UserCreateDTO):
    def __init__(self):
        super(UserUpdateDTO, self).__init__(partial=True)
