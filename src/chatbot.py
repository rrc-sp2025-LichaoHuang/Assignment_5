"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

import unittest
from unittest.mock import patch

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]
deposit_success = True
def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

def get_account_number() -> int:
    """
    The function prompts the user to input an account number, validates the input, and returns the account number as an integer. 
    The function is declared with no parameters.
    """
    # Get Account Number
    try:
        account_number = int(input("Please enter your account number:"))
        valid_account = account_number in ACCOUNTS.keys()
        if valid_account == False:
            print("Account number entered does not exist.")
        else:
            return account_number 
    except ValueError:
        print("Account number must be an int type.")
    

def get_amount() -> float:
    try:
        amount = float(input("Enter an amount::"))
        if amount <= 0:
            print("Amount must be a value greater than zero.")
            return
        else:
            print(f"${amount:,.2f}")
    except ValueError:
        print("Account number must be an int type.")
        return
    return amount


def get_balance(account_number: int = None):
    try:
        account_number = user_account_number
        if account_number in ACCOUNTS.keys():
            print(f"Your current balance for account {account_number} is ${ACCOUNTS[account_number]["balance"]:,.2f}.")
    except ValueError:
        print("Account number must be an int type.")


def make_deposit(account_number: int = None, amount: float = None) -> str:
        account_number = user_account_number
        global deposit_success
        amount = get_amount()
        if amount == None:
            deposit_success = False
            return
        ACCOUNTS[account_number]["balance"] += amount
        massage = f"You have made a deposit of ${amount:,.2f} to account {account_number}."
        return print(massage)


def get_task() -> str:
        
        task = (input("What would you like to do (balance/deposit/exit)?:"))
        lower_task = str.lower(task)
        print(lower_task)
        if lower_task in VALID_TASKS:
            return lower_task
        else:
            print(f'"{task}" is an unknown task.')
            return
        





#def test_get_account_number():
    # Arrange
   #with patch('builtins.input') as mock_input:
    # Act
    #mock_input.side_effect = [123456]
    # Assert

if __name__ == "__main__":
    chatbot()
    task = "none"
    while task != "exit":
        task = "none"
        task = get_task()
        if task in VALID_TASKS:
            if task == "exit":
                print("Thank you for banking with PiXELL River Financial.")
                break
            else:
                user_account_number = get_account_number()
                if task == "deposit":
                    deposit_success = True
                    make_deposit()
                    if deposit_success == False:
                        continue
                    get_balance()
                else:
                    get_balance()
        else:
            continue
