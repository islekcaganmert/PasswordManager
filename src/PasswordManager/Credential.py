class Credential:
    def __init__(self, username: str, password: str, notes: str) -> None:
        self.username: str = username
        self.password: str = password
        self.notes: str = notes
