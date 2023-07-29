  #Завдання на розробку об'єктно-орієнтованого програмного забезпечення (ООП) на мові Python, що передбачає створення CLI-додатку трекера витрат зі збереженням даних у файлі протоколом pickle та аналізом витрат/доходів за місяцями:
#Розробити клас Transaction, який буде представляти окрему транзакцію (витрату або дохід) з такими атрибутами:
#amount (float): сума транзакції.

#category (str): категорія транзакції.

#date (str): дата транзакції у форматі "РРРР-ММ-ДД".

#Розробити клас ExpenseTracker, який буде відповідати за управління трекером витрат. Він повинен мати такі методи:
#add_transaction(transaction: Transaction): додати нову транзакцію до трекера.

#remove_transaction(transaction: Transaction): видалити задану транзакцію з трекера.

#get_total_expenses() -> float: отримати загальну суму витрат.

#get_total_income() -> float: отримати загальну суму доходів.

#get_expenses_by_month(month: str) -> float: отримати суму витрат за заданий місяць.

#get_income_by_month(month: str) -> float: отримати суму доходів за заданий місяць.

#Розробити клас ExpenseTrackerApp, який буде представляти CLI-додаток трекера витрат. Він повинен мати такі методи:
#run(): запустити додаток та почати інтерактивний режим.

#load_data(file_path: str): завантажити дані про транзакції з файлу.

#save_data(file_path: str): зберегти дані про транзакції до файлу.

#Реалізувати функціональність додатку, де користувач може вводити команди для додавання/видалення транзакцій, отримання загальної суми витрат/доходів та отримання суми витрат/доходів за певний місяць.

#Забезпечити збереження даних про транзакції у файл за допомогою модуля pickle. При запуску додатку, перевірити, чи є збережений файл з даними, та завантажити їх, якщо вони існують.

#Реалізувати можливість виконання аналізу витрат/доходів за місяцями, шляхом обчислення суми транзакцій, які відповідають певному місяцю.

#Забезпечити зручний та зрозумілий інтерфейс для користувача, який дозволяє взаємодіяти з трекером витрат через команди та отримувати звіти про витрати/доходи за місяцями.

#Передбачити обробку помилок та виведення корисних повідомлень для користувача у випадку некоректних вхідних даних чи помилок виконання.

#Запрограмувати опцію вихідного пункту меню для користувача, що дозволяє зберегти дані та завершити роботу додатку.

#Забезпечити достатнє тестування програми, щоб переконатись у правильності її роботи та забезпечити надійність функцій трекера витрат.
import pickle

class Transaction:
    def __init__(self, amount: float, category: str, date: str) -> None:
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self) -> str:
        return f"Transaction: {self.category}, Amount: {self.amount}, Date: {self.date}"



class ExpenseTracker:
    def __init__(self) -> None:
        self.transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def remove_transaction(self, transaction: Transaction) -> None:
        self.transactions.remove(transaction)

    def get_total_expenses(self) -> float:
        return sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)

    def get_total_income(self) -> float:
        return sum(transaction.amount for transaction in self.transactions if transaction.amount >= 0)

    def get_expenses_by_month(self, month: str) -> float:
        return sum(transaction.amount for transaction in self.transactions
                   if transaction.amount < 0 and transaction.date.startswith(month))

    def get_income_by_month(self, month: str) -> float:
        return sum(transaction.amount for transaction in self.transactions
                   if transaction.amount >= 0 and transaction.date.startswith(month))

    def save_data(self, file_path: str) -> None:
        with open(file_path, 'wb') as file:
            pickle.dump(self.transactions, file)

    def load_data(self, file_path: str) -> None:
        with open(file_path, 'rb') as file:
            self.transactions = pickle.load(file)

class ExpenseTrackerApp:
    def __init__(self) -> None:
        self.tracker = ExpenseTracker()

    def run(self) -> None:
        print("Expense Tracker App - CLI Mode")
        print("Type 'help' or '?' for available commands.")
        while True:
            user_input = input("Enter command: ").strip()
            if user_input.lower() in ['exit', 'stop', 'close', '.']:
                self.tracker.save_data("transactions.pkl")
                print("Data saved. Exiting...")
                break
            self.execute_command(user_input)

    def execute_command(self, user_input: str) -> None:
        command, *args = user_input.split()

        if command == 'add':
            try:
                amount = float(args[0])
                category = args[1]
                date = args[2]
                transaction = Transaction(amount, category, date)
                self.tracker.add_transaction(transaction)
                print("Transaction added successfully.")
            except ValueError:
                print("Invalid input format for the 'add' command.")
            except IndexError:
                print("Insufficient arguments for the 'add' command.")
        elif command == 'remove':
            try:
                amount = float(args[0])
                category = args[1]
                date = args[2]
                transaction = Transaction(amount, category, date)
                self.tracker.remove_transaction(transaction)
                print("Transaction removed successfully.")
            except ValueError:
                print("Invalid input format for the 'remove' command.")
            except IndexError:
                print("Insufficient arguments for the 'remove' command.")
        elif command == 'total_expenses':
            print("Total expenses:", self.tracker.get_total_expenses())
        elif command == 'total_income':
            print("Total income:", self.tracker.get_total_income())
        elif command == 'expenses_by_month':
            try:
                month = args[0]
                print("Expenses for", month, ":", self.tracker.get_expenses_by_month(month))
            except IndexError:
                print("Insufficient arguments for the 'expenses_by_month' command.")
        elif command == 'income_by_month':
            try:
                month = args[0]
                print("Income for", month, ":", self.tracker.get_income_by_month(month))
            except IndexError:
                print("Insufficient arguments for the 'income_by_month' command.")
        elif command == 'help' or command == '?':
            self.print_help()
        else:
            print("Invalid command. Type 'help' or '?' for available commands.")

    @staticmethod
    def print_help() -> None:
        print("Available commands:")
        print("add <amount> <category> <date> - Add a new transaction")
        print("remove <amount> <category> <date> - Remove a transaction")
        print("total_expenses - Get total expenses")
        print("total_income - Get total income")
        print("expenses_by_month <month> - Get expenses for a specific month")
        print("income_by_month <month> - Get income for a specific month")
        print("exit - Save data and exit the app")


if __name__ == "__main__":
    tracker_app = ExpenseTrackerApp()
    try:
        tracker_app.tracker.load_data("transactions.pkl")
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No data found. Starting with an empty tracker.")
    tracker_app.run()