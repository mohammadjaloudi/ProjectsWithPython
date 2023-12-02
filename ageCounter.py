from datetime import datetime
import time
import os
import msvcrt

def calculate_age(birthdate):
    # Calculate age based on the difference between the birthdate and the current date
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today - birthdate

    # Break down the age into years, months, days, hours, minutes, and seconds
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    hours, remainder = divmod(age.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return years, months, days, hours, minutes, seconds

def display_age(age):
    # Display the calculated age in a formatted string, overwriting the previous line
    years, months, days, hours, minutes, seconds = age
    age_str = f"You are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
    print(age_str, end='\r')

def main():
    # Get the user's birthdate as input
    print("Welcome to the Age Counter!")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

    try:
        while True:
            # Record the start time of each iteration
            start_time = datetime.now()
            
            # Calculate and display the age, clearing the console screen first
            os.system('cls' if os.name == 'nt' else 'clear')
            age = calculate_age(birthdate_str)
            display_age(age)
            
            # Calculate the time elapsed since the start of the loop
            elapsed_time = datetime.now() - start_time
            sleep_time = max(0, 1 - elapsed_time.total_seconds())
            
            # Check if the Enter key is pressed to break out of the loop
            if msvcrt.kbhit() and msvcrt.getch() == b'\r':
                # Clear the screen before breaking
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
            # Pause for the remaining time to achieve a 1-second loop
            time.sleep(sleep_time)
    except ValueError:
        # Handle invalid date format input
        print("Invalid date format. Please use YYYY-MM-DD.")
    finally:
        # Clear the screen before exiting the program
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
