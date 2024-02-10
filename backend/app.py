"""Main start point for LiteStar API."""
import logging

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig, OpenAPIController

from api_app.controllers.apps import AppController
from api_app.controllers.categories import CategoryController
from api_app.controllers.rankings import RankingsController
from api_app.controllers.trackers import TrackersController

cors_config = CORSConfig(
    allow_origins=[
        "localhost",
    ],
)


class MyOpenAPIController(OpenAPIController):

    """Set Path for API docs."""

    path = "/api/docs"


logging_config = LoggingConfig(
    root={"level": logging.getLevelName(logging.INFO), "handlers": ["console"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
)


app = Litestar(
    route_handlers=[
        AppController,
        CategoryController,
        RankingsController,
        TrackersController,
    ],
    cors_config=cors_config,
    openapi_config=OpenAPIConfig(
        title="App Store API",
        version="0.0.1",
        openapi_controller=MyOpenAPIController,
    ),
    logging_config=logging_config,
    debug=True,
)
