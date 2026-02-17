import argparse
import math
import string
import sys

THRESHOLD = 3

parser = argparse.ArgumentParser(
    prog="password-evaluator",
    description="Determines the entropy of the provided password",
    epilog="Created by: Andrew McKenzie @ 2026",
    usage="%(prog)s [options] target"
)

parser.add_argument(
    "-p",
    "--password",
    type=str, 
    help="The password to evaluate"
)


def evaluate_difference(char_one: str, char_two: str) -> int:
    """
    Evaluates the difference between two characters.

    Args:
        char_one (str): The first character.
        char_two (str): The second character.
    
    Returns:
        int: The difference between the two characters.
    """
    return ord(char_two) - ord(char_one)


def evaluate_result(entropy_score: float) -> None:
    """
    Evaluates the entropy score and prints the result.

    Args:
        entropy_score (float): The entropy score.
    
    Returns:
        None
    """
    if entropy_score <= 28:
        print(f"Password: {args.password} is considered 'very weak'.")
    elif entropy_score <= 35:
        print(f"Password: {args.password} is considered 'weak'.")
    elif entropy_score <= 59:
        print(f"Password: {args.password} is considered 'moderate'.")
    elif entropy_score <= 127:
        print(f"Password: {args.password} is considered 'strong'.")
    else:
        print(f"Password: {args.password} is considered 'unbreakable'.")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.password is None:
        parser.print_help()
        sys.exit(1)
    
    previous_char = args.password[0]
    effective_length = len(args.password)
    current_streak = 1
    pool_size = 0
    found_items = ()
    streak_type = None
    
    # Determine pool size.
    for character in args.password:
        if character in string.ascii_lowercase and 'lower' not in found_items:
            pool_size += 26
            found_items += ('lower',)
        elif character in string.ascii_uppercase and 'upper' not in found_items:
            pool_size += 26
            found_items += ('upper',)
        elif character in string.digits and 'digit' not in found_items:
            pool_size += 10
            found_items += ('digit',)
        elif character in string.punctuation and 'punctuation' not in found_items:
            pool_size += 32
            found_items += ('punctuation',)

    for i in range(1, len(args.password)):
        current_char = args.password[i]
        diff = evaluate_difference(previous_char, current_char)

        if diff == 1 and streak_type == 'ascending':
            current_streak += 1
        elif diff == -1 and streak_type == 'descending':
            current_streak += 1
        elif diff == 0 and streak_type == 'repeat':
            current_streak += 1
        else:
            if current_streak >= THRESHOLD:
                effective_length -= (current_streak - 1)

            if diff == 1:
                streak_type = 'ascending'
                current_streak = 2
            elif diff == -1:
                streak_type = 'descending'
                current_streak = 2
            elif diff == 0:
                streak_type = 'repeat'
                current_streak = 2
            else:
                streak_type = None
                current_streak = 1
        
        previous_char = current_char

    
    # We must check if the password ended on a streak
    if current_streak >= THRESHOLD:
        effective_length -= (current_streak - 1)
    
    if pool_size > 0:
        entropy = effective_length * math.log2(pool_size)
        evaluate_result(entropy)
    else:
        print(f"Password: {args.password} is considered 'weak to moderate'.")