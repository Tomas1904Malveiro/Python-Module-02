class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)
    
def plants_error() -> None:
    raise PlantError("The tomato plant is wilting!")

def water_error() -> None:
    raise WaterError("Not enough water in the tank!")

def tests_garden_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        plants_error()
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    print("")
    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}")
    print("")
    print("Testing catching all garden errors...")
    try:
        plants_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        water_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    tests_garden_errors()