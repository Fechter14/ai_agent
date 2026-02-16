import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        to_run = ["python", file_path,]
        result = subprocess.run((to_run + args), capture_output=True, cwd=abs_working_directory, timeout=30, text=True)
        stdout = result.stdout
        stderr = result.stderr
        returncode = result.returncode
        
        output = []
        if stdout:
            output.append(f"STDOUT:\n{stdout}")
        if stderr:
            output.append(f"STDERR:\n{stderr}")
        if returncode != 0:
            output.append(f"Process exited with code {returncode}")
        
        if output:
            return "\n".join(output)
        else:
            return "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the Python file at specified file path and returns the output from the interpreter, constrained to the working directory, and passes arguments to it.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The location of the Python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file to be run.",
                ),
                description="An optional list of arguments to pass to the Python file to be run.",
            ),
        },
        required=["file_path"],
    ),
)