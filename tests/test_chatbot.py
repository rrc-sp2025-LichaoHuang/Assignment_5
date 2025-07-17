"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.chatbot. import ACCOUNTS, VALID_TASKS, get_account_number, get_amount, get_balance, get_task, make_deposit

__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class TestFunction(unittest.TestCase):
    def test_get_account_number_typeerror(self):
        with patch('builtins.input') as mock_input:
    # Arrange
            mock_input.side_effect = ["non_numeric_data"]
            expected = "Account number must be an int type."
    # Act
            actual = get_amount()
            self.assertEqual(expected, actual)
    
    def test_get_account_number_valueerror(self):
        with patch('builtins.input') as mock_input:
    # Arrange
            mock_input.side_effect = ["112233"]
            expected = "Account number entered does not exist."
    # Act
            actual = get_amount()
            self.assertEqual(expected, actual)
    def test_get_account_number_no_error(self):
        with patch('builtins.input') as mock_input:
    # Arrange
            mock_input.side_effect = ["123456"]
            expected = "123456"
    # Act
            actual = get_amount()
            self.assertEqual(expected, actual)

    
    



'''
    def test_get_balance():
        # Arrange
        # Act
        # Assert
    def test_make_deposit():
        # Arrange
        # Act
        # Assert
    def test_get_task():
        # Arrange
        # Act
        # Assert
'''