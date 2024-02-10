"""API endoipoints for app trackers.

/trackers/ returns list of top trackers.
"""

from typing import Self

from litestar import Controller, get
from litestar.exceptions import NotFoundException

from api_app.models import TopTrackers, TrackerApps
from config import get_logger
from dbcon.queries import get_apps_for_tracker, get_top_trackers

logger = get_logger(__name__)


def trackers_overview() -> TopTrackers:
    """Process trackers and return TopTrackers class."""
    df = get_top_trackers()
    df = df[~df["tracker_name"].isna()]
    df = df.sort_values("app_count", ascending=False)
    trackers = TopTrackers(trackers=df.to_dict(orient="records"))
    return trackers


class TrackersController(Controller):

    """API EndPoint return for app trackers."""

    path = "/api/trackers/"

    @get(path="/", cache=True)
    async def top_trackers(self: Self) -> TopTrackers:
        """Handle GET request for a list of top trackers.

        Returns
        -------
            A dictionary representation of the list of trackers
            each with an id, name, type and total of apps.

        """
        logger.info(f"{self.path} start")
        overview = trackers_overview()

        return overview

    @get(path="/{tracker_name:str}", cache=3600)
    async def get_tracker_apps(self: Self, tracker_name: str) -> TrackerApps:
        """Handle GET request for a specific tracker.

        Args:
        ----
            tracker_name (str): The name of the tracker to retrieve apps for.

        Returns:
        -------
            json

        """
        logger.info(f"{self.path} start")
        apps_df = get_apps_for_tracker(tracker_name)

        if apps_df.empty:
            msg = f"Store ID not found: {tracker_name!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        apps_dict = apps_df.to_dict(orient="records")

        apps = TrackerApps(
            title=tracker_name,
            apps=apps_dict,
        )
        return apps
