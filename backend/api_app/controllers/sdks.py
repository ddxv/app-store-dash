"""API endoipoints for sdks.

/sdks/overview returns list of all sdks.
"""

from typing import Self

from litestar import Controller, get

from api_app.models import (
    SdkCompanies,
    SdkOverview,
    SdksOverview,
)
from config import get_logger
from dbcon.queries import (
    get_sdk_pattern,
    get_sdk_pattern_companies,
    get_sdks,
)

logger = get_logger(__name__)


class SdksController(Controller):
    """API EndPoint return for all sdk related paths."""

    path = "/api/sdks"

    @get(path="/overview", cache=3600)
    async def sdks(self: Self) -> SdksOverview:
        """Handle GET request for all sdks.

        Returns
        -------
        SdksOverview
            An overview of sdks across different platforms and sources.

        """
        logger.info("GET /api/sdks/overview start")

        overview = get_sdks()

        is_google = overview["store"].str.startswith("Google")

        android_overview = overview[is_google]
        ios_overview = overview[~is_google]

        android_overview_dict = android_overview.to_dict(orient="records")
        ios_overview_dict = ios_overview.to_dict(orient="records")

        return SdksOverview(
            android_overview=android_overview_dict, ios_overview=ios_overview_dict
        )

    @get(path="/{value_pattern:str}", cache=3600)
    async def sdks_pattern(self: Self, value_pattern: str) -> SdkOverview:
        """Handle GET request for all sdks.

        Returns
        -------
        SdkOverview
            An overview of apps for a given sdk pattern.

        """
        logger.info(f"GET /api/sdks/{value_pattern} start")

        overview = get_sdk_pattern(value_pattern)

        is_google = overview["store"].str.startswith("Google")
        android_overview = overview[is_google]
        ios_overview = overview[~is_google]

        ios_overview_dict = ios_overview.to_dict(orient="records")
        android_overview_dict = android_overview.to_dict(orient="records")

        overview_resp = SdkOverview(
            ios_overview=ios_overview_dict, android_overview=android_overview_dict
        )

        return overview_resp

    @get(path="/{value_pattern:str}/companies", cache=3600)
    async def sdks_companies(self: Self, value_pattern: str) -> SdkCompanies:
        """Handle GET request for all sdks.

        Returns
        -------
        SdkOverview
            An overview of apps for a given sdk pattern.

        """
        logger.info(f"GET /api/sdks/{value_pattern}/companies start")

        overview = get_sdk_pattern_companies(value_pattern)

        overview_dict = overview.to_dict(orient="records")

        overview_resp = SdkCompanies(companies=overview_dict)

        return overview_resp
