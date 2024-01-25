class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        self.grade += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print("Engine started.")
            self.is_running = True
        else:
            print("Engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print("Engine stopped.")
            self.is_running = False
        else:
            print("Engine is already stopped.")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Running: {self.is_running}")


def main():
    # Example 1: Calculator
    calc = Calculator()
    result_add = calc.add(5, 3)
    result_subtract = calc.subtract(10, 4)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")

    # Example 2: Bank Account
    account1 = BankAccount("John Doe", 1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_balance()

    # Example 3: Student Information
    student1 = Student("Alice", 16, 10)
    student2 = Student("Bob", 15, 9)
    student1.promote()
    student1.display_info()
    student2.display_info()

    # Example 4: Book
    book1 = Book("Python Programming", "John Smith", 300)
    book2 = Book("Data Science Essentials", "Jane Doe", 250)
    book1.display_info()
    book2.display_info()

    # Example 5: Car
    car1 = Car("Toyota", "Camry", 2022)
    car1.start_engine()
    car1.display_info()
    car1.stop_engine()
    car1.display_info()


if __name__ == "__main__":
    main()
