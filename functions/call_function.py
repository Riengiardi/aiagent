import json
from collections.abc import Callable
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(tool_call, verbose: bool = False) -> dict:

    # getting function name and args (json string parsed to dict with 'loads()')
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    # if verbose respond with args else without
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    if not verbose:
        print(f" - Calling function: {function_name}")

    # defining function mapping
    function_map: dict[str, Callable[..., str]] = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "write_file" : write_file,
        "run_python_file" : run_python_file,
    }

    # checking whether function exists
    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }

    # defining working dir
    function_args["working_directory"] = "./calculator"

    # calling a function
    result = function_map[function_name](**function_args)

    # returning tool message
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }
    