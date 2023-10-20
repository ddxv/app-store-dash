from api_app.controllers.apps import AppController
from api_app.controllers.categories import CategoryController
from config import get_logger
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig

# from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig, OpenAPIController

cors_config = CORSConfig(
    allow_origins=[
        "https://apps.jamesoclaire.com",
        "https://www.jamesoclaire.com",
        "localhost",
        "*",
    ]
)

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
    route_handlers=[AppController, CategoryController],
    cors_config=cors_config,
    openapi_config=OpenAPIConfig(
        title="App Store API", version="0.0.1", openapi_controller=MyOpenAPIController
    ),
    logging_config=logging_config,
    debug=True,
)
