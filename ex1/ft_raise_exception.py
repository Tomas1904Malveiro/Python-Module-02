def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    valid_data = "25"
    print(f"Input data is '{valid_data}'")
    try:
        temp = input_temperature(valid_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    invalid_data = "abc"
    print("")
    print(f"Input data is '{invalid_data}'")
    try:
        temp = input_temperature(invalid_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    hot_data = "100"
    print("")
    print(f"Input data is '{hot_data}'")
    try:
        temp = input_temperature(hot_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    cold_data = "-50"
    print("")
    print(f"Input data is '{cold_data}'")
    try:
        temp = input_temperature(cold_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
