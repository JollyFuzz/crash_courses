from datetime import datetime
import pytz

WHITE = "\033[00m"
GREEN = "\033[0;92m"
RED = "\033[1;31m"

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.now())
        

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    
    def withraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            self.history.append((-amount, self._get_current_time()))
        else:
            print("Not enouth money")

        self.show_balance()

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction_name = "deposited"
                color = GREEN
            else:
                transaction_name = "withdraw"
                color = RED

            print(f"{color}{amount}{WHITE} {transaction_name} on {date.astimezone()}")


a = Account("Ivan", 0)
a.deposit(100)
a.deposit(100)
a.withraw(50)
a.show_history()
a.show_balance()
a.__balance = 10000
a.show_balance()
print(a.__balance)