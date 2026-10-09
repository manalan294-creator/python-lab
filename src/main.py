from utils import square, is_even, celsius_to_fahrenheit


def main():
    try:
        value = float(input("Enter a number in Celsius: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    result = "even" if is_even(value) else "odd"
    print(f"Square: {square(value)}")
    print(f"The number is {result}.")
    print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(value):.2f} F")


if __name__ == "__main__":
    main()
