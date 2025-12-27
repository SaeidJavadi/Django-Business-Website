from datetime import datetime as dt


def checkbirth(date):
    """
        Check if the person is at least 18 years old based on the given birthdate.
        Args:
        - date (str): Birthdate in "YYYY-MM-DD" format.
        Returns:
        - bool: True if the person is 18 or older, False otherwise.
        """
    try:
        # Convert the input date to string and strip time if present
        birth_date_str = str(date).split()[0]  # Remove time part if present
        # Remove time part from current date
        current_date_str = str(dt.now()).split()[0]

        # Convert the strings to datetime objects
        birth_date = dt.strptime(birth_date_str, "%Y-%m-%d")
        current_date = dt.strptime(current_date_str, "%Y-%m-%d")

        # Calculate the difference in days
        age_in_days = (current_date - birth_date).days

        # Check if the age is greater than or equal to 18 years (approx. 6570 days)
        if age_in_days >= 6570:
            return True
        else:
            return False
    except Exception as e:
        print('='*30)
        print(e)
        print('='*30)
        # Handle invalid input or errors
        return False


def checkidcode(value):
    a = int(value[-1])
    print(a)
    i = 0
    b = 0
    for num in reversed(range(2, 11)):
        b += int(value[i]) * num
        print(f'{value[i]}*{num}')
        i += 1
    c = b - (b / 11) * 11
    print(b, c)
    if c == 0 and a == c:
        return True
    elif c == 1 and a == 1:
        return True
    elif c > 1 and (a == c - 11):
        return True
    else:
        return False
