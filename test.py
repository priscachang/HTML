"""Simple demo script: main() calls helper functions that use loops."""


def sum_to(limit):
    """Return the sum of all integers from 1 up to (and including) limit."""
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


def fizzbuzz(limit):
    """Return a list of FizzBuzz labels for 1..limit."""
    labels = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            labels.append("FizzBuzz")
        elif number % 3 == 0:
            labels.append("Fizz")
        elif number % 5 == 0:
            labels.append("Buzz")
        else:
            labels.append(str(number))
    return labels


def countdown(start):
    """Count down from start to 1 using a while loop."""
    steps = []
    current = start
    while current > 0:
        steps.append(current)
        current -= 1
    return steps


def main():
    limit = 15

    print(f"Sum of 1..{limit} = {sum_to(limit)}")

    print("FizzBuzz:")
    for label in fizzbuzz(limit):
        print(f"  {label}")

    print(f"Countdown: {countdown(5)}")


if __name__ == "__main__":
    main()
