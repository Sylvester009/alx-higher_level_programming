#!/usr/bin/python3
def safe_print_integer(value):
  """
  prints an integer with "{:d}".format().
  value: any type (integer, string, etc.)
  Returns:
  True if value has been correctly printed
  otherwise false
  """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
