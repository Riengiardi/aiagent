import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        # checks if directory is in working_directory
        work_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(work_dir, file_path))
        is_valid_file = os.path.commonpath([work_dir, target_file]) == work_dir

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not is_valid_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        with open(target_file, 'r') as f:
            file_as_str = f.read(config.MAX_CHARS)
            if f.read(1):
                file_as_str += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'

        return file_as_str
    
    except Exception as e:
        print(e)

    
    

