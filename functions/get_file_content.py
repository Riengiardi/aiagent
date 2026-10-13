import os
from constants import *

def get_file_content(working_directory: str, file_path: str) -> str:

    try:

        # checking for valid target dir within working dir
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath((target_file, working_dir_abs)) == working_dir_abs
        
       # validation
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        # reading file 
        if valid_target_file:
            f = open(target_file)
            content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f'Error: {e}'

    