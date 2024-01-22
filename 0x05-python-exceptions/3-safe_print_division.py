def safe_print_division(a, b):
    """Returns: The value of the division, otherwise None."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
