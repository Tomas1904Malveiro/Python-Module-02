def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    valid_data = "25"
    print(f"Input data is {valid_data}")
    try:
        temp = input_temperature(valid_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    invalid_data = "abc"
    print(f"Input data is {invalid_data}")
    try:
        temp = input_temperature(invalid_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    test_temperature()
