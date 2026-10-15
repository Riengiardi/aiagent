import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try: 

        # abs file path
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # validating common path
        valid_target_path = os.path.commonpath((working_dir_abs, target_file_path)) == working_dir_abs

        # validating working dir
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_file_path[-3:] != '.py':
            return f'Error: "{file_path}" is not a Python file'

        # running file

        # creating command for subprocess
        command = ["python", target_file_path]
        if args != None:
            command.extend(args)

        # running command via subprocess
        cprocess = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        # creating output string
        if cprocess.returncode != 0:
            return f"Process exited with code {cprocess.returncode}\n"
        if cprocess.stdout == cprocess.stderr == None:
            return "No output produced"
        return f"STDOUT: {cprocess.stdout}\nSTDERR: {cprocess.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"

# OpenAI SDK JSON Schema for the function
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": (
            "Executes a Python (.py) file and returns its output. "
            "The file path must be relative to the working directory and must resolve inside it. "
            "The script runs with the working directory as its current directory and is killed if it runs longer than 30 seconds. "
            "Returns the captured STDOUT and STDERR, or the exit code if the script fails, "
            "or an error message if the file is missing, is not a .py file, or is outside the working directory."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path of the Python file to run, relative to the working directory "
                        "(e.g. 'main.py' or 'tests/test_calc.py'). Must end in '.py'."
                    ),
                },
                "args": {
                    "type": "array",
                    "description": (
                        "Optional command-line arguments passed to the script, one string per argument "
                        "(e.g. ['--verbose', '3 + 5']). Omit if the script takes no arguments."
                    ),

                },
            },
        },
    },
}