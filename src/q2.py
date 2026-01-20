"""
Please implement this stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""

import sys
sys.path.append('.')
from src.q1 import validate_password

def set_password() -> None:
    """
    1. Ask the user to input a password
    2. If it is not valid, print the 
       requirements which are not met and go back to step 1.
       (Keep repeating until password is valid)
    """
    # This function will require calling validate_password from q1
    arg = input("Enter a password: ")
    while validate_password(arg) is False:
        print("" \
        "Your password must be:" \
        "At least 8 characters long," \
        "have one uppercase letter," \
        "have one lowercase letter," \
        "have one number," \
        "and have one special character")
        arg = input("Enter a password: ")
        validate_password(arg)

