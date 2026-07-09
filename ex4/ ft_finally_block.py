class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def run_watering(plants: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)

    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    run_watering(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    run_watering(["Tomato", "lettuce", "Carrots"])

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()