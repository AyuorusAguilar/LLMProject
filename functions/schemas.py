schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory, providing file size and directory status, similar to ls in bash. It does not execute the files",
        "parameters": {
            "type": "object",
            "required": ["directory"],
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from (default is the working directory itself)",
                },
            },
        },
    },
}
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the first 10,000 characters of the content of a file",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file you'd like to rea e.g. 'content.txt' or 'pkg/python.py'",
                },
            },
        },
    },
}
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes inside a file, if a the given file_path already exists, writes inside that file, otherwise it creates it and writes inside it",
        "parameters": {
            "type": "object",
            "required": ["file_path", "content"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file you'd like to write on",
                },
                "content": {
                    "type": "string",
                    "description": "The content you'd like to write inside a file as a string",
                },
            },
        },
    },
}
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes/runs a python file with optional arguments",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the files you'd like to execute",
                },
                "args": {
                    "type": "array",
                    "description": "Arguments to call the python script with",
                    "items": {"type": "string"}
                },
            },
        },
    },
}