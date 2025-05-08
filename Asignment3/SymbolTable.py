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

        # Check for leading/trailing spaces or multiple spaces
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

            # Check for Redeclared error in the current block
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
            # def find_identifier(stack, name):
            #     for block in stack:
            #         if name in block:
            #             return block[name]
            #     return None
            find_identifier = lambda stack, name: next((block[name] for block in stack if name in block), None)

            identifier_type = find_identifier(stack, identifier_name)
            if identifier_type is None:
                return stack, [f"Undeclared: {command}"]

            # Determine the type of the value
            if value.isdigit():
                value_type = "number"
            elif value.startswith("'") and value.endswith("'") and value[1:-1].isalnum():
                value_type = "string"
            elif value[0].islower() and value.replace("_", "").isalnum():
                value_type = find_identifier(stack, value)
                if value_type is None:
                    return stack, [f"Undeclared: {command}"]
            else:
                return stack, [f"InvalidInstruction: {command}"]

            # Check for TypeMismatch error
            if identifier_type != value_type:
                return stack, [f"TypeMismatch: {command}"]

            return stack, results + ["success"]

        elif cmd_type == "BEGIN":
            # Push a new block onto the stack
            return [{}] + stack, results  # No "success" for BEGIN

        elif cmd_type == "END":
            # Pop the top block from the stack
            if len(stack) == 1:
                return stack, ["UnknownBlock"]  # Return only "UnknownBlock" and stop further processing
            return stack[1:], results  # No "success" for END

        elif cmd_type == "LOOKUP":
            if len(parts) != 2:
                return stack, [f"InvalidInstruction: {command}"]
            identifier_name = parts[1]

            # Validate identifier_name
            if not identifier_name[0].islower() or not identifier_name.replace("_", "").isalnum():
                return stack, [f"InvalidInstruction: {command}"]

            # Find the identifier in the stack
            # def find_level(stack, name):
            #     for i, block in enumerate(stack):
            #         if name in block:
            #             return i
            #     return None
            find_level = lambda stack, name: next((i for i, block in enumerate(stack) if name in block), None)

            level = find_level(stack, identifier_name)
            if level is None:
                return stack, results + [f"Undeclared: {command}"]

            # Append the block level to results
            return stack, results + [str(len(stack) - level - 1)]
        
        # new code very close
        elif cmd_type == "PRINT":
            # Collect all symbols in the stack in declaration order, considering redeclarations
            declared_order = []
            for block in reversed(stack):  # Iterate from the bottom-most block to the top-most block
                for name in block:
                    declared_order.append(name)  # Always add the name to preserve redeclaration order

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
            ReDeclared = []
            seen = set()
            for name in declared_order:
                if name in seen:
                    ReDeclared.append(name)
                else:
                    seen.add(name)

            # Construct the expected result
            expected_result = []
            for name in declared_order:
                if name in ReDeclared:
                    # Use the current level for redeclared identifiers
                    expected_result.append(f"{name}//{current_level}")
                else:
                    # Use the original level from symbols_to_print
                    for symbol in symbols_to_print:
                        if symbol.startswith(f"{name}//"):
                            expected_result.append(symbol)
                            break
            debut_result = []
            seen_redeclared = set()
            for symbol in expected_result:
                name = symbol.split("//")[0]
                if name in ReDeclared:
                    if name not in seen_redeclared:
                        seen_redeclared.add(name)
                        continue  # Skip the first occurrence
                debut_result.append(symbol)

            return stack, results + [
                # " ".join(declared_order), 
                # " ".join(symbols),
                # " ".join(symbols_to_print),
                # " ".join(expected_result),
                " ".join(debut_result),
            ]

        elif cmd_type == "RPRINT":
            # Collect all symbols in the stack in declaration order, considering redeclarations
            declared_order = []
            for block in reversed(stack):  # Iterate from the bottom-most block to the top-most block
                for name in block:
                    declared_order.append(name)  # Always add the name to preserve redeclaration order
            rev_declared_order = list(reversed(declared_order))
            # Collect all symbols in the stack 
            symbols = [
                f"{name}//{len(stack) - i - 1}"
                for i, block in enumerate(stack)
                for name in block
            ]
            # Arrange symbols in the declared order
            symbols_to_print = [
                symbol for name in rev_declared_order
                for symbol in symbols
                if symbol.startswith(f"{name}//")
            ]
            # Determine the current level of the PRINT command
            current_level = len(stack) - 1

            # Identify redeclared identifiers
            ReDeclared = []
            seen = set()
            for name in rev_declared_order:
                if name in seen:
                    ReDeclared.append(name)
                else:
                    seen.add(name)

            # Construct the expected result
            expected_result = []
            seen_names = set()  # Track already added names
            for name in rev_declared_order:
                if name in seen_names:
                    continue  # Skip if the name has already been added
                seen_names.add(name)  # Mark the name as added
                if name in ReDeclared:
                    # Use the current level for redeclared identifiers
                    expected_result.append(f"{name}//{current_level}")
                else:
                    # Use the original level from symbols_to_print
                    for symbol in symbols_to_print:
                        if symbol.startswith(f"{name}//"):
                            expected_result.append(symbol)
                            break
            return stack, results + [
                                    # " ".join(declared_order), 
                                    # " ".join(rev_declared_order), 
                                    # " ".join(symbols_to_print), 
                                    " ".join(expected_result),
                                    # " ".join(symbols)
                                    ]

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
    if len(final_stack) > 1 and all(r == "success" for r in final_results):
        return [f"UnclosedBlock: {len(final_stack) - 1}"]

    return final_results