import time

def countdown_timer(time_input):
    """
    Starts a countdown based on a 'HH:MM' formatted string.
    Converts the input to total seconds and displays the remaining time in HH:MM:SS format.
    """
    try:
        # Split the input string into hours and minutes, then convert to integers
        hours, minutes = map(int, time_input.split(':'))
        # Calculate the total number of seconds for the countdown
        total_seconds = hours * 3600 + minutes * 60
    except ValueError:
        # Handle invalid input formats (e.g., missing colon or non-numeric values)
        print("Invalid time format. Please enter time as HH:MM.")
        return

    # Loop from total_seconds down to 1, decrementing by 1 each iteration
    for remaining in range(total_seconds, 0, -1):
        # Compute full hours and the remaining seconds after hours
        hrs, rem = divmod(remaining, 3600)
        # Compute full minutes and the remaining seconds after minutes
        mins, secs = divmod(rem, 60)
        # Display the time left in HH:MM:SS format, updating on the same line
        print(f"{hrs:02}:{mins:02}:{secs:02} left", end='\r')
        # Pause execution for 1 second to create the countdown effect
        time.sleep(1)

    # After the loop ends, notify the user that the countdown is complete
    print("\nTime's up!")


if __name__ == "__main__":
    # Prompt the user for the countdown time when running the script directly
    time_input = input("Enter the time (HH:MM): ")
    countdown_timer(time_input)
