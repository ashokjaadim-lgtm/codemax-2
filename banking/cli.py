from banking.repository import AccountRepository
from banking.service import BankService


def read_amount(prompt: str) -> int:
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        raise ValueError("Please enter a whole number of rupees, for example 500.")


def run_app():
    bank = BankService(AccountRepository())
    print("\n=== OOP Banking System (Learning Project) ===")

    while True:
        print(
            "\n1. Create account\n"
            "2. Check account / balance\n"
            "3. Deposit money\n"
            "4. Withdraw money\n"
            "5. Transaction history\n"
            "0. Exit"
        )
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = input("Account holder name: ")
                opening = read_amount("Opening balance in INR (enter 0 if none): ")
                account = bank.create_account(name, opening)
                print(f"Account created! Account number: {account.account_number}")
                print(f"Current balance: ₹{account.balance}")

            elif choice == "2":
                number = input("Account number: ")
                account = bank.get_account(number)
                print(f"Name: {account.holder_name}")
                print(f"Account number: {account.account_number}")
                print(f"Balance: ₹{account.balance}")

            elif choice == "3":
                number = input("Account number: ")
                amount = read_amount("Deposit amount in INR: ₹")
                account = bank.deposit(number, amount)
                print(f"Deposit successful. New balance: ₹{account.balance}")

            elif choice == "4":
                number = input("Account number: ")
                amount = read_amount("Withdrawal amount in INR: ₹")
                account = bank.withdraw(number, amount)
                print(f"Withdrawal successful. New balance: ₹{account.balance}")

            elif choice == "5":
                number = input("Account number: ")
                history = bank.transaction_history(number)
                if not history:
                    print("No transactions yet.")
                else:
                    print("\n--- Transaction History ---")
                    for item in history:
                        print(
                            f"{item.timestamp} | {item.transaction_type:<8} | "
                            f"₹{item.amount} | Balance after: ₹{item.balance_after}"
                            + (f" | {item.note}" if item.note else "")
                        )

            elif choice == "0":
                print("Thank you for trying the project!")
                break

            else:
                print("Invalid option. Choose 0, 1, 2, 3, 4 or 5.")

        except (ValueError, RuntimeError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run_app()
