"""
Input Validation Decorators
Validate inputs before a function runs, without mixing validation code into business logic.
"""
def decorator(func):
    def wrapper(amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        return func(amount)
    return wrapper

@decorator
def withdraw(amount):
    print("withdrawn:",amount)
withdraw(200)
withdraw(100)


"""
concepts learned
validation logic
avoiding duplicate checks
"""

