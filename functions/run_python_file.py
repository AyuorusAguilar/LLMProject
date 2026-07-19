import os
import subprocess


def run_python_file(
	working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
	try:
		abs_working_directory = os.path.abspath(working_directory)
		final_path = os.path.normpath(os.path.join(abs_working_directory, file_path))
		is_valid = os.path.commonpath([abs_working_directory, final_path]) == abs_working_directory
		if not is_valid:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
		if not os.path.isfile(final_path):
			return f'Error: "{file_path}" does not exist or is not a regular file'
		if final_path[-2:] != 'py':
			return f'Error: "{file_path}" is not a Python file'
		
		command = ["python", final_path]
		if args:
			command.extend(args)

		result = subprocess.run(command, cwd=os.path.dirname(final_path), capture_output=True, text=True, timeout=30)
		output_str = ''
		if result.returncode != 0:
			output_str += f"Process exited with code {result.returncode}"
		if not result.stdout and not result.stderr:
			output_str += "No output produced"
		else:
			output_str += f"STDOUT: {result.stdout}"
			output_str += f"STDERR: {result.stderr}"
		return output_str
	except Exception as e:
		return f"Error: executing Python file: {e}"