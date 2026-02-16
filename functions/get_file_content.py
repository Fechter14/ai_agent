import os
from config import CHARLIMIT
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(CHARLIMIT)

        if len(file_content_string) == CHARLIMIT:
            file_content_string += f'[...File "{file_path}" truncated at {CHARLIMIT} characters]'
        
        return file_content_string
    
    except Exception as e:
        return f"Error reading file: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content of files truncated to a {CHARLIMIT} character limit, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The location of the file to retrieve content from, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)