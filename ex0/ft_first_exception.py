def check_temperature(temp_str: str):
    try:
        tmp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if tmp_int > 40:
            print(f"Error: {tmp_int}°C is too hot for plants (max 40°C)")
        elif tmp_int < 0:
            print(f"Error: {tmp_int}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {tmp_int}°C is perfect for plants!")
def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    i = 0
    while i < 4:
        temp_str = input("Testing temperature: ")
        check_temperature(temp_str)
        print()
        i += 1
    
    print("All tests completed - program didn't crash!")
    
        
if __name__ == "__main__":
    test_temperature_input()
    
    
