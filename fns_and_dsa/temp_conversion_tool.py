CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter temperature: "))
        unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

        if unit == 'C':
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        elif unit == 'F':
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        else:
            print("Invalid unit. Use 'C' or 'F'.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
