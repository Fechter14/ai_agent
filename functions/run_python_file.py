import os, subprocess

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