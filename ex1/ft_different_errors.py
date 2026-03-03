def garden_operations() -> None:
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    
    try:
        print("\nTesting ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        f = open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        
    try:
        print("\nTesting KeyError...")
        dict = {'key': 5}
        dict['missing_plant']
    except KeyError:
        print("Caught KeyError: 'missing\_plant'")
    try:
        print("\nTesting multiple errors together...")
        1 / 0
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
    
    
    
        