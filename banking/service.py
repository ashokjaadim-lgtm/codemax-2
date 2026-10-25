from banking.models import Account, Transaction
from banking.repository import AccountRepository


class BankService:
    """Business rules for account creation, deposits, withdrawals and history."""

    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, holder_name: str, opening_balance: int = 0) -> Account:
        holder_name = holder_name.strip()
        if not holder_name:
            raise ValueError("Account holder name cannot be empty.")
        if not isinstance(opening_balance, int) or isinstance(opening_balance, bool):
            raise ValueError("Amount must be a whole number of rupees.")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        account = Account(
            account_number=self.repository.next_account_number(),
            holder_name=holder_name,
            balance=opening_balance,
        )
        if opening_balance > 0:
            account.transactions.append(
                Transaction.create("DEPOSIT", opening_balance, opening_balance, "Opening balance")
            )
        self.repository.save(account)
        return account

    def _get_account_or_raise(self, account_number: str) -> Account:
        account = self.repository.get(account_number.strip())
        if account is None:
            raise ValueError("Account not found. Check the account number.")
        return account

    @staticmethod
    def _validate_amount(amount: int) -> None:
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise ValueError("Amount must be a whole number of rupees.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def get_account(self, account_number: str) -> Account:
        return self._get_account_or_raise(account_number)

    def deposit(self, account_number: str, amount: int) -> Account:
        self._validate_amount(amount)
        account = self._get_account_or_raise(account_number)
        account.balance += amount
        account.transactions.append(Transaction.create("DEPOSIT", amount, account.balance))
        self.repository.save(account)
        return account

    def withdraw(self, account_number: str, amount: int) -> Account:
        self._validate_amount(amount)
        account = self._get_account_or_raise(account_number)
        if amount > account.balance:
            raise ValueError("Insufficient balance.")
        account.balance -= amount
        account.transactions.append(Transaction.create("WITHDRAW", amount, account.balance))
        self.repository.save(account)
        return account

    def transaction_history(self, account_number: str) -> list[Transaction]:
        account = self._get_account_or_raise(account_number)
        return list(account.transactions or [])
