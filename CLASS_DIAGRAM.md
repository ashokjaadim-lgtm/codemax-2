# Class Diagram

```mermaid
classDiagram
    class Account {
        +str account_number
        +str holder_name
        +int balance
        +list transactions
        +to_dict()
        +from_dict(data)
    }

    class Transaction {
        +str transaction_type
        +int amount
        +int balance_after
        +str timestamp
        +str note
        +create(type, amount, balance, note)
        +to_dict()
        +from_dict(data)
    }

    class AccountRepository {
        +get(account_number)
        +save(account)
        +all_accounts()
        +next_account_number()
    }

    class BankService {
        +create_account(holder_name, opening_balance)
        +get_account(account_number)
        +deposit(account_number, amount)
        +withdraw(account_number, amount)
        +transaction_history(account_number)
    }

    class CLI {
        +run_app()
        +read_amount(prompt)
    }

    Account "1" *-- "0..*" Transaction : contains
    BankService --> AccountRepository : uses
    AccountRepository ..> Account : loads/saves
    AccountRepository ..> Transaction : loads/saves
    CLI --> BankService : calls
```

## Architecture

- **Models (`models.py`)**: Defines account and transaction data.
- **Repository (`repository.py`)**: Reads and writes JSON data.
- **Service (`service.py`)**: Contains validation and banking business rules.
- **CLI (`cli.py`)**: Displays the menu and reads user input.
- **Entry point (`main.py`)**: Starts the application.
