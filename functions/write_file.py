import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
	try:
		abs_working_directory = os.path.abspath(working_directory)
		final_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
		is_valid = os.path.commonpath([abs_working_directory, final_path]) == abs_working_directory
		if not is_valid:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
		if os.path.isdir(final_path):
			return f'Error: Cannot write to "{file_path}" as it is a directory'
		
		os.makedirs(os.path.dirname(final_path), exist_ok=True)
		with open(final_path, 'w') as file:
			file.write(content)
		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	except Exception as e:
		return f'Error: Found the following exception:\n{e}'