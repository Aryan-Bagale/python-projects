import time

def countdown_timer(time_input):
    try:
        hours, minutes = map(int, time_input.split(':'))
        total_seconds = (hours * 3600) + (minutes * 60)
    except ValueError:
        print("Invalid time format. Please enter time as HH:MM.")
        return

    for remaining in range(total_seconds, 0, -1):
        hrs, rem = divmod(remaining, 3600)
        mins, secs = divmod(rem, 60)
        print(f"{hrs:02}:{mins:02}:{secs:02} left", end='\r')
        time.sleep(1)
    
    print("\nTime's up!")

if __name__ == "__main__":
    time_input = input("Enter the time (HH:MM): ")
    countdown_timer(time_input)