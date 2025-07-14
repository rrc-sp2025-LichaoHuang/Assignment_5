"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

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

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

def get_account_number():
    """
    The function prompts the user to input an account number, validates the input, and returns the account number as an integer. 
    The function is declared with no parameters.
    """
    # Get Account Number
    try:
        account_number = 0
        account_number = int(input("Please enter your account number:"))
        valid_account = account_number in ACCOUNTS.keys()
        if valid_account == False:
            print("Account number entered does not exist.")
        else:
            print(account_number)
            
    except ValueError:
        print("Account number must be an int type.")


        


if __name__ == "__main__":
    chatbot()
    get_account_number()
