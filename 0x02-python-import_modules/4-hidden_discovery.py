#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by hidden_4.pyc"""

    import hidden_4

    names = dir(hidden_4)
    for lists in names:
        if lists[:2] != "__":
            print(lists)
