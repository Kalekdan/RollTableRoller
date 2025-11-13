"""
Roll Table Roller utility for D&D and RPG random table generation.

This module provides functionality to roll on tables with support for:
- Dice rolls (e.g., [d20])
- Nested table references (e.g., [examples/creatures.txt])
- Inline selections (e.g., {option1,option2,option3})
"""
import re
from random import randrange

DEMO_TABLE = 'examples/example.txt'


def roll_parser(ref):
    """
    Parse and resolve dice rolls or nested table references.

    Args:
        ref: A regex match object containing the bracketed expression.

    Returns:
        str: The resolved value (either a dice roll result or table roll result).
    """
    string_value = ref.group(0)[1:-1]
    # if dice roll
    dice_roll = re.search(r"d\d+", string_value)
    if dice_roll is not None:
        num = int(dice_roll.group(0)[1:])
        return str(randrange(1, num + 1))
    # otherwise return table value
    return roll_table(string_value).strip()


def selection_parser(val):
    """
    Parse and randomly select from inline comma-separated choices.

    Args:
        val: A regex match object containing the braced expression.

    Returns:
        str: A randomly selected choice from the list.
    """
    string_value = val.group(0)[1:-1]
    choices = string_value.split(",")
    return choices[randrange(len(choices))]


def line_parser(line_to_parse):
    """
    Parse a line and resolve all bracketed and braced expressions.

    Args:
        line_to_parse: A string containing expressions to parse.

    Returns:
        str: The line with all expressions resolved.
    """
    keys = re.sub(r'\[.*?\]', roll_parser, line_to_parse)
    keys = re.sub(r'\{.*?\}', selection_parser, keys)
    return keys


def roll_table(table_name=DEMO_TABLE):
    """
    Roll on a random table and return a parsed result.

    Args:
        table_name: Path to the table file relative to the tables directory.

    Returns:
        str: A randomly selected and parsed line from the table.

    Raises:
        FileNotFoundError: If the table file does not exist.
        IOError: If there is an error reading the table file.
    """
    table_path = "tables/" + table_name
    with open(table_path, encoding='utf-8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        line_rolled = randrange(num_lines)
        line = lines[line_rolled]
        line = line_parser(line)
    return line


if __name__ == "__main__":
    # Example usage
    print(roll_table("examples/example.txt"))
