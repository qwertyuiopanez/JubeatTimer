import time

def increment_counter():
    try:
        # Get the starting value for the counter from the user
        counter = int(input("Current Stamina: ")
        time.sleep(3 * 60)
        while True:
            counter += 1
            print(f"Stamina: {counter}")
            time.sleep(3 * 60)  # Sleep for 3 minutes (3 * 60 seconds)
    except ValueError:
        print("Invalid input. Please enter an integer for the starting value.")
    except KeyboardInterrupt:
        print("\nProgram stopped.")
        print(f"Final stamina: {counter}")

if __name__ == "__main__":
    increment_counter()
