class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class WaterError(Exception):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)
    
def plants_error() -> None:
    raise PlantError("The tomato plant is wilting!")

def water_error() -> None:
    raise WaterError("Not enough water in the tank!")

def tests_Garden_Errors():
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")