from mongoengine import connect, NotUniqueError
from sanic import Sanic
from sanic.response import empty

from sanic_hello.controller.user_controller import bp as user_controller

app = Sanic("Test Sanic Framework")
app.config.FALLBACK_ERROR_FORMAT = "json"
app.error_handler.add(NotUniqueError, lambda req, ex: empty(status=409))
app.blueprint(user_controller)

connect(db="sanic_hello")

if __name__ == "__main__":  # pragma: no cover
    app.run(port=4000)
