class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.water_tank = 10

    def add_plant(self, plants_list: list[Plant]) -> None:
        try:
            for plant in plants_list:
                if plant.plant_name == "" or plant.plant_name is None:
                    raise PlantError("Plant name cannot be empty!")
                self.plants.append(plant)
                print(f"Added {plant.plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                plant.water_level += 5
                print(f"Watering {plant.plant_name} - success")
                self.water_tank -= 5
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                if plant.water_level > 10:
                    raise WaterError(f"Water level {plant.water_level} "
                                     "is too high (max 10)")
                elif plant.water_level < 1:
                    raise WaterError(f"Water level {plant.water_level} "
                                     "is too low (min 1)")
                if plant.sunlight_hours > 12:
                    raise PlantError(f"Sunlight hours {plant.sunlight_hours} "
                                     "is too high (max 12)")
                elif plant.sunlight_hours < 2:
                    raise PlantError(f"Sunlight hours {plant.sunlight_hours} "
                                     "is too low (min 2)")
                print(f"{plant.plant_name}: healthy (water: "
                      f"{plant.water_level}, sun: {plant.sunlight_hours})")
        except GardenError as e:
            print(f"Error checking {plant.plant_name}: {e}")

    def check_tank(self) -> None:
        try:
            if self.water_tank <= 0:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            while self.water_tank <= 0:
                self.water_tank += 5
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()
    plants_list = [
        Plant("tomato", 0, 8),
        Plant("lettuce", 10, 10),
        Plant("", 8, 10)
        ]
    print("\nAdding plants to garden...")
    manager.add_plant(plants_list)
    print("\nWatering plants...")
    manager.water_plants()
    print("\nChecking plant health...")
    manager.check_plant_health()
    print("\nTesting error recovery...")
    manager.check_tank()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(f"Error: {e}")
