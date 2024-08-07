class ZombieDefError(Exception):
    def __init__(self, error_code: int, error_message: str):
        self.error_code = error_code
        self.error_message = error_message

        super().__init__(f"(Error Code - {error_code}) {error_message}")


class UnknownZombieDefError(Exception):
    ...


class RealmNotFoundError(ZombieDefError):
    ...


class RegistrationEndedError(ZombieDefError):
    ...


class GameNotStartedError(ZombieDefError):
    ...


class PlayerNotParticipatingInRound(ZombieDefError):
    ...


class MethodNotFoundError(ZombieDefError):  # 1
    ...
