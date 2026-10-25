import json
from pathlib import Path
from banking.models import Account


class AccountRepository:
    """Stores accounts in a local JSON file for this learning project."""

    def __init__(self, file_path: str = "data/accounts.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("{}", encoding="utf-8")

    def _read_all(self) -> dict:
        try:
            return json.loads(self.file_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            raise RuntimeError("Could not read account data. Check data/accounts.json.")

    def _write_all(self, data: dict) -> None:
        self.file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def get(self, account_number: str) -> Account | None:
        data = self._read_all()
        account_data = data.get(account_number)
        return Account.from_dict(account_data) if account_data else None

    def save(self, account: Account) -> None:
        data = self._read_all()
        data[account.account_number] = account.to_dict()
        self._write_all(data)

    def all_accounts(self) -> list[Account]:
        data = self._read_all()
        return [Account.from_dict(item) for item in data.values()]

    def next_account_number(self) -> str:
        accounts = self.all_accounts()
        largest = max((int(a.account_number) for a in accounts), default=100000)
        return str(largest + 1)
