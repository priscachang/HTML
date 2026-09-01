"""Simple demo script: main() calls helper functions that use loops."""


def sum_to(limit: int) -> int:
    """Return the sum of all integers from 1 up to (and including) limit."""
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


def fizzbuzz(limit: int) -> list[str]:
    """Return a list of FizzBuzz labels for 1..limit."""
    labels: list[str] = []
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


def countdown(start: int) -> list[int]:
    """Count down from start to 1 using a while loop."""
    steps: list[int] = []
    current = start
    while current > 0:
        steps.append(current)
        current -= 1
    return steps


def _format_demo_output(limit: int = 15, countdown_start: int = 5) -> str:
    """Create the same text the original demo printed, as a single string."""
    lines: list[str] = []

    lines.append(f"Sum of 1..{limit} = {sum_to(limit)}")

    lines.append("FizzBuzz:")
    for label in fizzbuzz(limit):
        lines.append(f"  {label}")

    lines.append(f"Countdown: {countdown(countdown_start)}")

    return "\n".join(lines)


def main(args):
    """StackAI Code Node entrypoint.

    Reads optional configuration from args and returns the demo output.
    """
    # Optional inputs (safe defaults)
    limit = args.get("limit", 15) if isinstance(args, dict) else 15
    countdown_start = args.get("countdown_start", 5) if isinstance(args, dict) else 5

    output_text = _format_demo_output(limit=limit, countdown_start=countdown_start)

    return {
        "limit": limit,
        "sum": sum_to(limit),
        "fizzbuzz": fizzbuzz(limit),
        "countdown": countdown(countdown_start),
        "output": output_text,
        # Convenience if you want to access the fetched file content:
        "source_from_action_0": (
            args.get("nodes", {}).get("action-0", {}).get("content")
            if isinstance(args, dict)
            else None
        ),
    }
