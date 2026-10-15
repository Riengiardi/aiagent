import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        # getting target file abspath
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # getting common path between target file and work dir abs
        valid_target_file = os.path.commonpath((target_file, working_dir_abs)) == working_dir_abs

        # work dir validation logic
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # making sure that all dirs exist
        target_dir = os.path.dirname(target_file)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
            
        # writing file
        f = open(target_file, mode='w')
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"

# OpenAI SDK JSON Schema for the function
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": (
            "Creates a new file or completely overwrites an existing file with the given content. "
            "Any existing content in the file is replaced, not appended to. "
            "Missing parent directories are created automatically. "
            "The path must be relative to the working directory and must resolve inside it; "
            "paths outside the working directory, or paths that point to a directory, are rejected with an error. "
            "Returns a success message with the number of characters written, or an error message."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path of the file to create or overwrite, relative to the working directory "
                        "(e.g. 'notes.txt' or 'src/utils/helpers.py'). "
                        "Must not point outside the working directory or to an existing directory."
                    ),
                },
                "content": {
                    "type": "string",
                    "description": (
                        "The full text to write to the file. This becomes the entire file contents, "
                        "so include everything that should be in the file, not just the changes."
                    ),
                },
            },
        },
    },
}
