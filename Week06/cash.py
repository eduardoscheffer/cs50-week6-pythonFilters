from cs50 import get_float

def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    total = quarters + dimes + nickels + pennies
    print(total)

main()

def get_cents():
    while True:
        change = get_float("How many change? ")
        if change >= 0:
            break
    cents = change * 100
    return cents

def calculate_quarters(cents):
    count = 0
    while(cents >= 25):
        cents = cents - 25
        count += 1
    return count

def calculate_dimes(cents):
    count = 0
    while (cents >= 10):
        cents = cents - 10
        count += 1
    return count

def calculate_nickels(cents):
    count = 0
    while (cents >= 5):
        cents = cents - 5
        count += 1
    return count

def calculate_pennies(cents):
    count = 0
    while (cents >= 1):
        cents = cents - 1
        count += 1
    return count