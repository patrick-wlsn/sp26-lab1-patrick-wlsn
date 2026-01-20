"""
Please implement these stub functions to match the documentation.
Make sure to implement tests in the tests directory.
"""


def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    #1.)
    if len(password) < 8:
        return False

    #2.)
    upper = 0
    for u in password:
        if u.isupper():
            upper += 1
    if upper == 0:
        return False
    
    #3.)
    lower = 0
    for l in password:
        if l.islower():
            lower += 1
    if lower == 0:
        return False
    
    #4.)
    numb = 0
    for n in password:
        if int(n):
            numb += 1
    if numb == 0:
        return False
    
    #5.)
    spechar = 0
    spec = ["!", "@", "#", "$", "%", "^", "&", "*"]
    for s in password:
        if s in spec:
            spechar += 1
    if spechar == 0:
        return False
    
    return True
