import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
	try:
		abs_working_directory = os.path.abspath(working_directory)
		final_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
		is_valid = os.path.commonpath([abs_working_directory, final_path]) == abs_working_directory
		if not is_valid:
			return f'Error: Cannot read "{final_path}" as it is outside the permitted working directory'
		if os.path.isdir(final_path):
			return f'Error: File not found or is not a regular file: "{final_path}"'
		with open(final_path, 'r') as file:
			content = file.read(10000)
			if file.read(1) != '':
				content += f'[...File "{final_path}" truncated at {10000} characters]'
		return content
	except Exception as e:
		return f'Error: Found the following exception:\n{e}'