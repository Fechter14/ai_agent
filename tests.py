#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
    '''

if __name__ == "__main__":
    test()