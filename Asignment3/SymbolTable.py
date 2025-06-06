from StaticError import *
from Symbol import *
from functools import *

def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """
    def process_command(state, command):
        stack, results = state

        # Check leading/trailing spaces or multiple spaces
        if command.strip() != command or "  " in command:
            return stack, [f"InvalidInstruction: {command}"]

        parts = command.split()

        # Skip invalid commands with incorrect number of parts
        if len(parts) < 1:
            return stack, [f"InvalidInstruction: {command}"]

        cmd_type = parts[0]

        if cmd_type == "INSERT":
            if len(parts) != 3:
                return stack, [f"InvalidInstruction: {command}"]
            _, identifier_name, typ = parts

            # Validate identifier_name and type
            if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
                return stack, [f"InvalidInstruction: {command}"]
            if typ not in ["number", "string"]:
                return stack, [f"InvalidInstruction: {command}"]

            # Check Redeclared error in the current block
            current_block = stack[0]
            if identifier_name in current_block:
                return stack, [f"Redeclared: {command}"]

            # Insert into the current block
            new_block = {**current_block, identifier_name: typ}
            new_stack = [new_block] + stack[1:]
            return new_stack, results + ["success"]

        elif cmd_type == "ASSIGN":
            if len(parts) != 3:
                return stack, [f"InvalidInstruction: {command}"]
            _, identifier_name, value = parts

            # Find the identifier in the stack
            find_identifier = lambda stack, name: next(filter(lambda block: name in block, stack), {}).get(name, None)

            identifier_type = find_identifier(stack, identifier_name)
            if identifier_type is None:
                return stack, [f"Undeclared: {command}"]

            # Determine the type of the value
            # if value.isdigit():
            #     value_type = "number"
            # elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
            #     value_type = "string"
            # elif value[0].islower() and value.replace("_", "").isalnum():
            #     value_type = find_identifier(stack, value)
            #     if value_type is None:
            #         return stack, [f"Undeclared: {command}"]
            # else:
            #     return stack, [f"InvalidInstruction: {command}"]

            # # Check TypeMismatch error
            # if identifier_type != value_type:
            #     return stack, [f"TypeMismatch: {command}"]
            
            # if value.isdigit():
            #     number_type = "number"
            # elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
            #     string_type = "string"
            # elif value[0].islower() and value.replace("_", "").isalnum():
            #     referenced_type = find_identifier(stack, value)
            #     if referenced_type is None:
            #         return stack, [f"Undeclared: {command}"]
            # else:
            #     return stack, [f"InvalidInstruction: {command}"]

            # # Assign the determined type to a new variable
            # if value.isdigit():
            #     determined_type = number_type
            # elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
            #     determined_type = string_type
            # else:
            #     determined_type = referenced_type

            # # Check TypeMismatch error
            # if identifier_type != determined_type:
            #     return stack, [f"TypeMismatch: {command}"]

            # return stack, results + ["success"]
            if value.isdigit():
                number_type = "number"
                if identifier_type != number_type:
                    return stack, [f"TypeMismatch: {command}"]
            elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
                string_type = "string"
                if identifier_type != string_type:
                    return stack, [f"TypeMismatch: {command}"]
            elif value[0].islower() and value.replace("_", "").isalnum():
                referenced_type = find_identifier(stack, value)
                if referenced_type is None:
                    return stack, [f"Undeclared: {command}"]
                if identifier_type != referenced_type:
                    return stack, [f"TypeMismatch: {command}"]
            else:
                return stack, [f"InvalidInstruction: {command}"]

            # If no errors, return success
            return stack, results + ["success"]

        elif cmd_type == "BEGIN":
            # Push a new block onto the stack
            return [{}] + stack, results  # No "success" BEGIN

        elif cmd_type == "END":
            # Pop the top block from the stack
            if len(stack) == 1:
                return stack, ["UnknownBlock"]  # Return only "UnknownBlock" and stop further processing
            return stack[1:], results  # No "success" END

        elif cmd_type == "LOOKUP":
            if len(parts) != 2:
                return stack, [f"InvalidInstruction: {command}"]
            identifier_name = parts[1]

            # Validate identifier_name
            if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
                return stack, [f"InvalidInstruction: {command}"]

            # Find the identifier in the stack
            find_level = lambda stack, name: next(map(lambda x: x[0], filter(lambda x: name in x[1], enumerate(stack))), None)

            level = find_level(stack, identifier_name)
            if level is None:
                return stack, [f"Undeclared: {command}"]  # Return immediately on error

            # Append the block level to results
            return stack, results + [str(len(stack) - level - 1)]

        elif cmd_type == "PRINT":
            # Collect all symbols in the stack in declaration order, considering redeclarations
            declared_order = reduce(lambda acc, block: acc + list(block.keys()), reversed(stack), [])

            # Generate the symbols with their levels
            symbols = [
                f"{name}//{len(stack) - i - 1}"
                for i, block in enumerate(stack)
                for name in block
            ]

            # Arrange symbols in the declared order
            symbols_to_print = [
                symbol for name in declared_order
                for symbol in symbols
                if symbol.startswith(f"{name}//")
            ]

            # Determine the current level of the PRINT command
            current_level = len(stack) - 1

            # Identify redeclared identifiers
            ReDeclared = [name for name in declared_order if declared_order.count(name) > 1]

            # Construct the expected result
            expected_result = [
                f"{name}//{current_level}" if name in ReDeclared else next(
                    symbol for symbol in symbols_to_print if symbol.startswith(f"{name}//")
                )
                for name in declared_order
            ]

            seen_redeclared = set()

            def include_symbol(symbol):
                name = symbol.split("//")[0]
                if name in ReDeclared:
                    # If it's the first encountered instance, add to the set and exclude the symbol.
                    if name not in seen_redeclared:
                        seen_redeclared.add(name)
                        return False
                return True

            debut_result = list(filter(include_symbol, expected_result))

            return stack, results + [" ".join(debut_result)]

        elif cmd_type == "RPRINT":
            # Collect all symbols in the stack in declaration order, considering redeclarations
            declared_order1 = reduce(lambda acc, block: acc + list(block.keys()), reversed(stack), [])

            # Reverse the order of the declaration
            rev_declared_order = list(reversed(declared_order1))

            # Collect all symbols in the stack
            symbols1 = [
                f"{name}//{len(stack) - i - 1}"
                for i, block in enumerate(stack)
                for name in block
            ]

            # Arrange symbols in the declared order
            symbols_to_print1 = [
                symbol for name in rev_declared_order
                for symbol in symbols1
                if symbol.startswith(f"{name}//")
            ]

            # Determine the current level of the PRINT command
            current_level1 = len(stack) - 1

            # Identify redeclared identifiers
            ReDeclared1 = [name for name in rev_declared_order if name in set() or set().add(name)]

            # Construct the expected result
            seen_names = set()
            expected_result1 = [
                f"{name}//{current_level1}" if name in ReDeclared1 else next(
                    symbol for symbol in symbols_to_print1 if symbol.startswith(f"{name}//")
                )
                for name in rev_declared_order
                if name not in seen_names and not seen_names.add(name)
            ]

            return stack, results + [" ".join(expected_result1)]

        return stack, [f"InvalidInstruction: {command}"]

    # Use reduce to process all commands
    def reducer(state, command):
        stack, results = state
        # If the last result is an error (except for LOOKUP), stop processing
        if results and results[-1] not in ["success"] and not results[-1].isdigit():
            return state
        return process_command(state, command)

    initial_state = ([{}], [])
    final_stack, final_results = reduce(reducer, list_of_commands, initial_state)

    # Check for unclosed blocks only if no errors occurred
    if len(final_stack) > 1 and all(map(lambda r: r == "success", final_results)):
        return [f"UnclosedBlock: {len(final_stack) - 1}"]

    return final_results