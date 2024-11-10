from PasswordManager.Credential import Credential
from PasswordManager.AES import AES
import json


class Vault:
    def __init__(self, data: tuple[callable, callable], master_password: str) -> None:
        self.master_password: str = master_password
        self.data: tuple[callable, callable] = data
        self.salt: str = ""
        self._credentials: dict[str, list[str, str, str]] = {}  # domain: [username, password, notes]
        self.load()

    def add_credentials(self, domain: str, username: str, password: str) -> None:
        self._credentials.update({domain: [username, password, '']})

    def get_credentials(self, domain: str) -> Credential:
        return Credential(*self._credentials[domain])

    def save(self) -> None:
        encrypted_data = {
            "credentials": AES.encrypt(json.dumps(self._credentials), self.master_password, self.salt),
            "salt": self.salt
        }
        self.data[1](encrypted_data)

    def load(self) -> None:
        encrypted_data = self.data[0]()
        if encrypted_data != {}:
            self.salt = encrypted_data['salt']
            self._credentials = json.loads(AES.decrypt(encrypted_data['credentials'], self.master_password, self.salt))
        else:
            self.salt = AES.generate_salt()

    def remove_credential(self, domain: str) -> None:
        self._credentials.pop(domain)

    def get_credential_count(self, domain: str) -> int:
        return len(self._credentials)
