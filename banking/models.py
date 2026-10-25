from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any


@dataclass
class Transaction:
    transaction_type: str
    amount: int
    balance_after: int
    timestamp: str
    note: str = ""

    @classmethod
    def create(cls, transaction_type: str, amount: int, balance_after: int, note: str = ""):
        return cls(
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
            timestamp=datetime.now().astimezone().isoformat(timespec="seconds"),
            note=note,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Transaction":
        return cls(**data)


@dataclass
class Account:
    account_number: str
    holder_name: str
    balance: int = 0
    transactions: list[Transaction] | None = None

    def __post_init__(self):
        if self.transactions is None:
            self.transactions = []

    def to_dict(self) -> dict[str, Any]:
        return {
            "account_number": self.account_number,
            "holder_name": self.holder_name,
            "balance": self.balance,
            "transactions": [transaction.to_dict() for transaction in self.transactions or []],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Account":
        return cls(
            account_number=data["account_number"],
            holder_name=data["holder_name"],
            balance=int(data["balance"]),
            transactions=[Transaction.from_dict(item) for item in data.get("transactions", [])],
        )
