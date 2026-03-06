def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise TypeError("invalid plant")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: Cannot water {plant} - {e}!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    list_normal = ["tomato", "lettuce", "carrots"]
    water_plants(list_normal)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    list_error = ["tomato", None, "carrots"]
    water_plants(list_error)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(f"Error: {e}")
