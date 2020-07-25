def check_email(string):
    no_white_space = ' ' not in string
    contains_at = '@' in string

    start = string.index('@')
    ends_with_dot = string.endswith('.com')

    if no_white_space and contains_at and ends_with_dot:
        return True
    else:
        return False