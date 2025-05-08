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

# working for INSERT
# def simulate(list_of_commands):
#     """
#     Executes a list of commands and processes them sequentially.

#     Args:
#         list_of_commands (list[str]): A list of commands to be executed.

#     Returns:
#         list[str]: A list of return messages corresponding to each command.
#     """
#     def process_command(state, command):
#         symbol_table, results = state
#         parts = command.split()

#         # Skip invalid commands
#         if len(parts) != 3 or parts[0] != "INSERT":
#             return symbol_table, results

#         _, identifier_name, typ = parts

#         # Validate identifier_name and type
#         if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
#             return symbol_table, results
#         if typ not in ["number", "string"]:
#             return symbol_table, results

#         # Check for Redeclared error
#         if identifier_name in symbol_table:
#             return symbol_table, [f"Redeclared: {command}"]

#         # Insert into symbol table
#         new_symbol_table = {**symbol_table, identifier_name: typ}
#         return new_symbol_table, results + ["success"]

#     # Use reduce to process all commands
#     _, results = reduce(process_command, list_of_commands, ({}, []))
#     return results

# INSER + ASSIGN unchecked valid
# def simulate(list_of_commands):
#     """
#     Executes a list of commands and processes them sequentially.

#     Args:
#         list_of_commands (list[str]): A list of commands to be executed.

#     Returns:
#         list[str]: A list of return messages corresponding to each command.
#     """
#     def process_command(state, command):
#         symbol_table, results = state
#         parts = command.split(maxsplit=2)

#         # Skip invalid commands
#         if len(parts) < 2:
#             return symbol_table, results

#         cmd_type = parts[0]

#         if cmd_type == "INSERT":
#             if len(parts) != 3:
#                 return symbol_table, results
#             _, identifier_name, typ = parts

#             # Validate identifier_name and type
#             if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
#                 return symbol_table, results
#             if typ not in ["number", "string"]:
#                 return symbol_table, results

#             # Check for Redeclared error
#             if identifier_name in symbol_table:
#                 return symbol_table, [f"Redeclared: {command}"]

#             # Insert into symbol table
#             new_symbol_table = {**symbol_table, identifier_name: typ}
#             return new_symbol_table, results + ["success"]

#         elif cmd_type == "ASSIGN":
#             if len(parts) != 3:
#                 return symbol_table, results
#             _, identifier_name, value = parts

#             # Check if identifier_name is declared
#             if identifier_name not in symbol_table:
#                 return symbol_table, [f"Undeclared: {command}"]

#             # Determine the type of the value
#             if value.isdigit():
#                 value_type = "number"
#             elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
#                 value_type = "string"
#             elif value in symbol_table:
#                 value_type = symbol_table[value]
#             else:
#                 return symbol_table, [f"Undeclared: {command}"]

#             # Check for TypeMismatch error
#             if symbol_table[identifier_name] != value_type:
#                 return symbol_table, [f"TypeMismatch: {command}"]

#             # Assignment is successful
#             return symbol_table, results + ["success"]

#         # If command is invalid or not recognized
#         return symbol_table, results

#     # Use reduce to process all commands and stop on the first error
#     def reducer(state, command):
#         symbol_table, results = state
#         if results and "success" not in results[-1]:
#             return state  # Stop processing if an error has already occurred
#         return process_command(state, command)

#     _, results = reduce(reducer, list_of_commands, ({}, []))
#     return results

# check valid
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

        # Check for leading/trailing spaces or multiple spaces
        if command.strip() != command or "  " in command:
            return symbol_table, [f"InvalidInstruction: {command}"]

        parts = command.split()

        # Skip invalid commands with incorrect number of parts
        if len(parts) < 2:
            return symbol_table, [f"InvalidInstruction: {command}"]

        cmd_type = parts[0]

        if cmd_type == "INSERT":
            if len(parts) != 3:
                return symbol_table, [f"InvalidInstruction: {command}"]
            _, identifier_name, typ = parts

            # Validate identifier_name and type
            if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
                return symbol_table, [f"InvalidInstruction: {command}"]
            if typ not in ["number", "string"]:
                return symbol_table, [f"InvalidInstruction: {command}"]

            # Check for Redeclared error
            if identifier_name in symbol_table:
                return symbol_table, [f"Redeclared: {command}"]

            # Insert into symbol table
            new_symbol_table = {**symbol_table, identifier_name: typ}
            return new_symbol_table, results + ["success"]

        elif cmd_type == "ASSIGN":
            if len(parts) != 3:
                return symbol_table, [f"InvalidInstruction: {command}"]
            _, identifier_name, value = parts

            # Check if identifier_name is declared
            if identifier_name not in symbol_table:
                return symbol_table, [f"Undeclared: {command}"]

            # Determine the type of the value
            if value.isdigit():
                value_type = "number"
            elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
                value_type = "string"
            elif value in symbol_table:
                value_type = symbol_table[value]
            else:
                return symbol_table, [f"Undeclared: {command}"]

            # Check for TypeMismatch error
            if symbol_table[identifier_name] != value_type:
                return symbol_table, [f"TypeMismatch: {command}"]

            # Assignment is successful
            return symbol_table, results + ["success"]

        # If command is invalid or not recognized
        return symbol_table, [f"InvalidInstruction: {command}"]

    # Use reduce to process all commands and stop on the first error
    def reducer(state, command):
        symbol_table, results = state
        if results and "success" not in results[-1]:
            return state  # Stop processing if an error has already occurred
        return process_command(state, command)

    _, results = reduce(reducer, list_of_commands, ({}, []))
    return results