#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    '''
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for 'pkg' directory:")
    print(result)
    
    result = get_file_content("calculator", "Lorem.txt")
    print(f"Lorem.txt length: {len(result)}")
    print(result[-100:])

    result = get_file_content("calculator", "main.py")
    print(f"Main.py length: {len(result)}")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Calculator.py length: {len(result)}")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(f"Result for /bin/cat:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for does_not_exist.py:")
    print(result)
    
    result = write_file("calculator", "Lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result for Lorem.txt:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result for morelorem.txt:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result for temp.txt:")
    print(result)
    '''
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print(result)

if __name__ == "__main__":
    test()