# Python OOP Banking System

A beginner-friendly command-line banking simulation built with Python and Object-Oriented Programming (OOP). It is suitable as a learning project for a Python internship/module deliverable.

## Features

- Create a bank account
- Generate a unique account number
- Check account details and balance
- Deposit money
- Withdraw money with insufficient-balance validation
- View transaction history with date/time and balance after each transaction
- Save account data locally in a JSON file
- Unit tests using Python's built-in `unittest`

## Important note

This is an **educational demo**, not real banking software. It has no login, encryption, authorization, audit controls, or connection to a bank. Do not store real customer or financial information in it.

## Requirements

- Python 3.10 or newer
- No third-party packages required

Check Python:

```bash
python --version
```

## Run the project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal (`Terminal` → `New Terminal`).
4. Run:

```bash
python main.py
```

On some Windows systems, use `py main.py`.

The program creates `data/accounts.json` automatically when it first runs.

## Menu

```text
1. Create account
2. Check account / balance
3. Deposit money
4. Withdraw money
5. Transaction history
0. Exit
```

### Example test flow

1. Choose `1`, enter `Ashok`, and opening balance `1000`.
2. Note the account number shown on screen.
3. Choose `3`, enter that account number, and deposit `500`.
4. Choose `4`, enter the account number, and withdraw `200`.
5. Choose `5` to see transaction history.

The expected balance after this flow is **₹1,300**.

## Run unit tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

## OOP concepts demonstrated

- **Class:** `Account`, `Transaction`, `AccountRepository`, `BankService`
- **Object:** Individual account and transaction instances
- **Encapsulation:** Banking rules and validation are handled by `BankService`
- **Abstraction:** The CLI calls service methods without needing to know how JSON storage works
- **Composition:** An `Account` contains a list of `Transaction` objects
- **Separation of concerns:** Models, repository, service logic, and CLI are in separate files

Inheritance and polymorphism are core OOP topics, but are not forced into this small project where they would add unnecessary complexity.

## Project structure

```text
python-oop-banking-system/
├── banking/
│   ├── __init__.py
│   ├── cli.py
│   ├── models.py
│   ├── repository.py
│   └── service.py
├── data/
│   └── accounts.json       # generated at runtime; ignored by Git
├── tests/
│   ├── __init__.py
│   └── test_bank.py
├── .gitignore
├── CLASS_DIAGRAM.md
├── README.md
└── main.py
```

## Suggested GitHub repository description

`A beginner-friendly Python OOP banking system with account creation, deposits, withdrawals, transaction history, JSON persistence, and unit tests.`

## Suggested GitHub topics

`python`, `oop`, `banking-system`, `beginner-project`, `json`, `unittest`

## Push to GitHub

Create an empty repository on GitHub, then run these commands in the VS Code terminal from this folder:

```bash
git init
git add .
git commit -m "Build Python OOP banking system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the example URL with your own repository URL. Do not upload passwords, API keys, or real customer data.
