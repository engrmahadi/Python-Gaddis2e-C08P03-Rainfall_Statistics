__author__ = 'dwight'


def validate_rainfall(rainfall, month):
    while not _is_number(rainfall) or float(rainfall) < 0:
        if not _is_number(rainfall):
            rainfall = input('Invalid input. Please re-enter value for ' + month + ': ')
        elif float(rainfall) < 0:
            rainfall = input('Rainfall cannot be negative. Please re-enter value for ' + month + ': ')

    return rainfall


def _is_number(test_input):
    try:
        float(test_input)
        return True
    except ValueError:
        return False
