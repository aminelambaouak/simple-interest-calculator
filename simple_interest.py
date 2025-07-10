# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Args:
        principal (float): The principal amount.
        rate (float): Annual interest rate (in percent).
        time (float): Time in years.

    Returns:
        float: Simple interest.
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    # Sample usage
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time in years: "))
    interest = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {interest}")
