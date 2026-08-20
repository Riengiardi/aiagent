import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:

        work_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(work_dir, file_path))
        is_valid_file = os.path.commonpath([work_dir, target_file]) == work_dir

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        if not is_valid_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")