import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:     

        # check for commonpath
        work_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(work_dir, file_path))
        is_valid_path = os.path.commonpath([work_dir, target_path]) == work_dir

        # guardrail for invalid paths
        if not is_valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        # command for subprocess + check for None args
        command = ["python", target_path]
        if args:
            command.extend(args)

        sub = subprocess.run(command, capture_output=True, timeout=30, text=True)

        result = ''

        if sub.returncode != 0:
            result += f"Proces exited with code {sub.returncode}"
        if sub.stdout == '' and sub.stderr == '':
            result += f"\nNo output produced"
        else:
            result += f"\nSTDOUT: {sub.stdout}\nSTDERR: {sub.stderr}"

        return result
    
    except Exception as e:
        print(f"Error: {e}")



    