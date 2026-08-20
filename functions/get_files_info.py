import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:

        # checks if directory is in working_directory
        work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir, directory))
        is_valid_dir = os.path.commonpath([work_dir, target_dir]) == work_dir

        # checks if directory is proper
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # terminates if directory is outside working_directory
        if not is_valid_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        print(f'Success: "{directory}" is within the working directory')
        
        result = "Result for current directory:"

        for item in os.listdir(target_dir):
            check_dir = os.path.join(target_dir, item)
            result += f"\n - {item}: file_size={os.path.getsize(check_dir)} bytes, is_dir={os.path.isdir(check_dir)}"

        return result    
            
    except Exception as e: 
        print(f"Error: {e}")