from cs50 import get_string

# Here's a list of tuples:
presidents = {
    "George Washington": 1789,
    "John Adams": 1797,
    "Thomas Jefferson": 1801,
    "James Madison": 1809
}

prez = get_string("What president you want to know? ")

if prez in presidents:
    print(f"In {presidents[prez]}, {prez} took office.")

