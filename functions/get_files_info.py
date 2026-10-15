import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        # checking for valid target dir within working dir
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath((target_dir, working_dir_abs)) == working_dir_abs

        # validation
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # returning contents
        file_list = os.listdir(target_dir)
        contents = ''
        for file in file_list:
            file_dir_abs = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_dir_abs)
            is_dir = os.path.isdir(file_dir_abs)
            contents += f'- {file}: file_size={file_size} bytes, is_dir={is_dir}\n'
        return contents[:-1]

        
    except Exception as e:
        return f'Error: {e}'

# OpenAI SDK JSON Schema for the function
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": (
            "Lists the files and subdirectories directly inside a directory (not recursive). "
            "The directory must be relative to the working directory and must resolve inside it. "
            "Defaults to the working directory itself if no directory is given. "
            "Returns one line per entry in the form '- name: file_size=N bytes, is_dir=True/False', "
            "or an error message if the path is not a directory or is outside the working directory. "
            "Use this to explore the project structure before reading, writing, or running files."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": (
                        "Path of the directory to list, relative to the working directory "
                        "(e.g. 'src' or 'tests/unit'). Use '.' or omit to list the working directory itself."
                    ),
                },
            },
        },
    },
}