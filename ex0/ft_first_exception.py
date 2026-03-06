def check_temperature(temp_str: str) -> int:
    try:
        try:
            tmp_int = int(temp_str)
        except ValueError:
            raise ValueError(f"'{temp_str}' is not a valid number")
        if tmp_int > 40:
            raise ValueError(f"{tmp_int}°C is too hot for plants (max 40°C)")
        elif tmp_int < 0:
            raise ValueError(f"{tmp_int}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        return tmp_int


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    test = ["25", "abc", "100", "-50"]
    for tmp_str in test:
        print(f"\nTesting temperature: {tmp_str}")
        tmp_int = check_temperature(tmp_str)
        if tmp_int is not None:
            print(f"Temperature {tmp_int}°C is perfect for plants!")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Error: {e}")
