from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # return for reuse in future calculation


def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)  # Add days
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    try:
        days_input = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


if __name__ == "__main__":
    main()
