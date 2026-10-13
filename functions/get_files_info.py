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
        if valid_target_dir:
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