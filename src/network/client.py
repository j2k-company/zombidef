from urllib.parse import urljoin
from requests import HTTPError, JSONDecodeError, Response, Session

from src.exceptions import ZombieDefError, UnknownZombieDefError, RealmNotFoundError
from src.model.command import Command
from src.model.game import Game
from src.model.unit import Units
from src.model.world import World


TEST_BASE_URL = "https://games-test.datsteam.dev/"
BASE_URL = "https://games.datsteam.dev/"


class Client():
    """main client for interacting with server"""

    def __init__(self, token: str, test: bool = False):
        self.base_url = TEST_BASE_URL if test else BASE_URL
        self._session = Session()
        self._session.headers.update({
            "X-Auth-Token" : token,
            "Content-type" : "application/json"
        })

    def check_for_errors(self, response: Response):
        try:
            response.raise_for_status()
        except HTTPError as e:
            try:
                data = response.json()
                error_code = data["errCode"]
                error_message = data["error"]
                print(error_code, error_code == 23)

                if error_code == 23:
                    raise RealmNotFoundError(error_code, error_message) from e
                raise ZombieDefError(error_code, error_message) from e

            except (KeyError, JSONDecodeError) as ue:
                raise UnknownZombieDefError() from ue

    def safe_get(self, endpoint: str) -> Response:
        """safety send get requests to server"""

        response = self._session.get(urljoin(self.base_url, endpoint))
        self.check_for_errors(response)

        return response

    def safe_post(self, endpoint: str, data: dict) -> Response:
        """safety send post requests to server"""

        response = self._session.post(urljoin(self.base_url, endpoint), data=data)
        self.check_for_errors(response)

        return response

    def safe_put(self, endpoint: str) -> Response:
        """safety send get requests to server"""

        response = self._session.put(urljoin(self.base_url, endpoint))
        self.check_for_errors(response)

        return response

    def send_command(self, command: Command) -> tuple[Command, str]:
        response = self.safe_post(
            "/play/zombidef/command/",
            command.to_request()
        ).json()

        return (
            Command.from_json(str(response["acceptedCommands"])),
            response["errors"]
        )

    def participate(self) -> int:
        return self.safe_put("/play/zombidef/participate").json()["startsInSec"]

    def get_units(self) -> Units:
        response = self.safe_get("/play/zombidef/units")
        return Units.from_json(response.text)

    def research_world(self) -> World:
        response = self.safe_get("/play/zombidef/world")
        return World.from_json(response.text)

    def get_rounds(self) -> Game:
        response = self.safe_get("/rounds/zombidef")
        return Game.from_json(response.text)
