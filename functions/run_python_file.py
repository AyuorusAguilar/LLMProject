import os


def run_python_file(
	working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
	abs_working_directory = os.path.abspath(working_directory)
	final_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
	is_valid = os.path.commonpath([abs_working_directory, final_path]) == abs_working_directory
	if not is_valid:
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'