import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_directory = os.path.abspath(working_directory)
        final_path = os.path.normpath(os.path.join(abs_working_directory, directory))
        if not os.path.isdir(final_path):
            return f'Error: "{directory}" is not a directory'
        is_valid = os.path.commonpath([final_path, abs_working_directory]) == abs_working_directory
        if not is_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error:Found the following exception:\n{e}'