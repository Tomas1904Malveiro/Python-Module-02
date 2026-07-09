def graden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        0 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operator = 0
    print("Testing operation 0...")
    try:
        graden_operations(operator)
        print("Operation completed successfully")
    except ValueError as err:
        print(f"Caught ValueError: {err}")
    operator = 1
    print("Testing operation 1...")
    try:
        graden_operations(operator)
        print("Operation completed successfully")
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
    operator = 2
    print("Testing operation 2...")
    try:
        graden_operations(operator)
        print("Operation completed successfully")
    except FileNotFoundError as err:
        print(f"Caught FileExistsError: {err}")
    operator = 3
    print("Testing operation 3...")
    try:
        graden_operations(operator)
        print("Operation completed successfully")
    except TypeError as err:
        print(f"Caught TypeError: {err}")
    operator = 4
    print("Testing operation 4...")
    graden_operations(operator)
    print("Operation completed successfully")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
