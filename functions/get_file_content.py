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
        f = open(target_file)
        content = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

    except Exception as e:
        return f'Error: {e}'

# OpenAI SDK JSON Schema for the function
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": (
            "Reads and returns the text contents of a file. "
            "The file path must be relative to the working directory and must resolve inside it. "
            "Large files are truncated after a fixed number of characters (MAX_CHARS), "
            "and a note is appended at the end of the output when this happens, "
            "so a truncated result does not contain the whole file. "
            "Returns an error message if the file does not exist, is not a regular file, "
            "or is outside the working directory. "
            "Use get_files_info first if you are unsure of the exact path."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path of the file to read, relative to the working directory "
                        "(e.g. 'main.py' or 'src/utils/helpers.py')."
                    ),
                },
            },
        },
    },
}

    