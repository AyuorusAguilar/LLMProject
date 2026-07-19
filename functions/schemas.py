schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the first 10,000 characters of a text file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file_path path to the file you'd like to read",
                },
            },
        },
    },
}
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Overwirtes or creates a file with the content provided",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file_path path to the files you'd like to write on",
                },
                "content": {
                    "type": "string",
                    "description": "The content you like to write over the file",
                },
            },
        },
    },
}
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file with optional arguments",
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