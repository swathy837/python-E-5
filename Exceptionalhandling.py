class ExceptionDemo:
    def handle_zero_division(self):
        try:
            num = float(input("Enter numerator: "))
            den = float(input("Enter denominator: "))
            result = num / den
            print("Result is", result)
        except ZeroDivisionError:
            print("Error: You cannot divide a number by zero.")

    def handle_value_error(self):
        try:
            val = int(input("Enter an integer: "))
            print("You entered the number", val)
        except ValueError:
            print("Error: That was not a valid integer.")

    def handle_index_error(self):
        try:
            items = ["Apple", "Banana", "Cherry"]
            print("Available indices are 0, 1, 2")
            idx = int(input("Enter an index to access: "))
            print("Item at index", idx, "is", items[idx])
        except IndexError:
            print("Error: The index you entered is out of range.")

    def handle_key_error(self):
        try:
            data = {"name": "swathy", "age": 24}
            print("Available keys: name, age")
            key = input("Enter a key to find: ")
            print("The value for", key, "is", data[key])
        except KeyError:
            print("Error: The key", key, "does not exist in the dictionary.")
demo = ExceptionDemo()
demo.handle_zero_division()
demo.handle_value_error()
demo.handle_index_error()
demo.handle_key_error()
