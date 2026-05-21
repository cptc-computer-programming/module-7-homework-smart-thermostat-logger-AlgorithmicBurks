MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76


def get_number_of_readings() -> int:
    while True:
        readings = int(input("Enter the number of temperature readings: "))
        print("Error: The number of readings must be greater than 0.")

    if readings > 0:
        return readings

        print("Error: The number of readings must be greater than 0.")


def get_valid_temperature(reading_number: int) -> int:
    while True:
            temperature = int(input(f"Enter temperature reading {reading_number}: "))
 
            print("Error: Temperature must be between 40 and 100 degrees.")


    if MIN_VALID_TEMP <= temperature <= MAX_VALID_TEMP:
        return temperature

        print("Error: Temperature must be between 40 and 100 degrees.")


def main() -> None:
    total_temp = 0
    below_comfort_count = 0
    above_comfort_count = 0

    number_of_readings = get_number_of_readings()

    for reading_index in range(1, number_of_readings + 1):
        temperature = get_valid_temperature(reading_index)
        total_temp += temperature



    average_temp = total_temp / number_of_readings

    print()
    print("Smart Thermostat Summary")
    print("------------------------")
    print(f"Average temperature: {format(average_temp, '.1f')}")
    print(f"Readings below comfort range: {below_comfort_count}")
    print(f"Readings above comfort range: {above_comfort_count}")


if __name__ == "__main__":
    main()