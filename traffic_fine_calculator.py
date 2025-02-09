def calculate_fine(speed, speed_limit, is_signal_violation):
    """
    Calculate traffic fine based on speed, speed limit, and signal violation.
    
    Args:
        speed (int): Speed of the vehicle.
        speed_limit (int): Speed limit for the road.
        is_signal_violation (bool): Whether the driver broke a signal.

    Returns:
        fine (int): The calculated fine.
    """
    fine = 0

    # Check if speed crossed the limit
    if speed > speed_limit:
        excess_speed = speed - speed_limit
        fine += excess_speed * 10  # Fine $10 for each km/h over the limit

    # Additional fine for breaking a traffic signal
    if is_signal_violation:
        fine += 200  # Signal violation fine is $200

    return fine


# Input from the user
try:
    speed = int(input("Enter the vehicle speed (in km/h): "))
    speed_limit = int(input("Enter the speed limit (in km/h): "))
    signal_violation = input("Did the driver break a signal? (yes/no): ")

    # Convert signal violation input to a boolean
    is_signal_violation = signal_violation.lower() == "yes"

    # Calculate fine
    fine = calculate_fine(speed, speed_limit, is_signal_violation)

    # Display the result
    print(f"Total Fine: ${fine}")

except ValueError:
    print("Please enter valid number inputs for speed and speed limit.")