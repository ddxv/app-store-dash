"""API endoipoints for app networks.

/networks/ returns list of top networks.
"""

from typing import Self

from litestar import Controller, get
from litestar.exceptions import NotFoundException

from api_app.models import NetworkApps, TopNetworks
from config import get_logger
from dbcon.queries import get_apps_for_network, get_top_companies

logger = get_logger(__name__)


def networks_overview() -> TopNetworks:
    """Process networks and return TopNetworks class."""
    df = get_top_companies(categories=[1])
    df = df[~df["name"].isna()]
    df = df.sort_values("app_count", ascending=False)
    networks = TopNetworks(networks=df.to_dict(orient="records"))
    return networks


class NetworksController(Controller):

    """API EndPoint return for app networks."""

    path = "/api/networks/"

    @get(path="/", cache=True)
    async def top_networks(self: Self) -> TopNetworks:
        """Handle GET request for a list of top networks.

        Returns
        -------
            A dictionary representation of the list of networks
            each with an id, name, type and total of apps.

        """
        logger.info(f"{self.path} start")
        overview = networks_overview()

        return overview

    @get(path="/{network_name:str}", cache=3600)
    async def get_network_apps(self: Self, network_name: str) -> NetworkApps:
        """Handle GET request for a specific network.

        Args:
        ----
            network_name (str): The name of the network to retrieve apps for.

        Returns:
        -------
            json

        """
        logger.info(f"{self.path} start")
        apps_df = get_apps_for_network(network_name)

        if apps_df.empty:
            msg = f"Network Name not found: {network_name!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        apps_dict = apps_df.to_dict(orient="records")

        apps = NetworkApps(
            title=network_name,
            apps=apps_dict,
        )
        return apps
