from StaticError import *
from Symbol import *
from functools import *

# class Redeclared(Exception):
#     def __init__(self, command):
#         super().__init__(f"Redeclared: {command}")

# def simulate(list_of_commands):
#     """
#     Executes a list of commands and processes them sequentially.

#     Args:
#         list_of_commands (list[str]): A list of commands to be executed.

#     Returns:
#         list[str]: A list of return messages corresponding to each command.
#     """
#     symbol_table = {}  # Dictionary to store symbols with their types
#     results = []

#     for command in list_of_commands:
#         parts = command.split()
#         if len(parts) != 3 or parts[0] != "INSERT":
#             continue  # Skip invalid commands

#         _, identifier_name, typ = parts

#         # Validate identifier_name and type
#         if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
#             continue  # Skip invalid identifiers
#         if typ not in ["number", "string"]:
#             continue  # Skip invalid types

#         # Check for Redeclared error
#         if identifier_name in symbol_table:
#             return [f"Redeclared: {command}"]  # Return immediately with the error

#         # Insert into symbol table
#         symbol_table[identifier_name] = typ
#         results.append("success")

#     return results
def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """
    def process_command(state, command):
        symbol_table, results = state
        parts = command.split()

        # Skip invalid commands
        if len(parts) != 3 or parts[0] != "INSERT":
            return symbol_table, results

        _, identifier_name, typ = parts

        # Validate identifier_name and type
        if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
            return symbol_table, results
        if typ not in ["number", "string"]:
            return symbol_table, results

        # Check for Redeclared error
        if identifier_name in symbol_table:
            return symbol_table, [f"Redeclared: {command}"]

        # Insert into symbol table
        new_symbol_table = {**symbol_table, identifier_name: typ}
        return new_symbol_table, results + ["success"]

    # Use reduce to process all commands
    _, results = reduce(process_command, list_of_commands, ({}, []))
    return results