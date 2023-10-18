from litestar import Litestar

# from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig, OpenAPIController

from litestar.logging import LoggingConfig

from api_app.controllers.apps import AppController

from config import get_logger

logger = get_logger(__name__)


class MyOpenAPIController(OpenAPIController):
    path = "/api/docs"


logging_config = LoggingConfig(
    loggers={
        "my_app": {
            "level": "INFO",
            "handlers": ["queue_listener"],
        }
    }
)

app = Litestar(
    route_handlers=[AppController],
    openapi_config=OpenAPIConfig(
        title="App Store API", version="0.0.1", openapi_controller=MyOpenAPIController
    ),
    logging_config=logging_config,
    debug=True,
)
