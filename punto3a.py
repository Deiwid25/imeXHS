import threading
import time

def print_even_numbers():
  """Function to print even numbers from 1 to 200."""
  for num in range(0, 199, 2):  # Start at 0 and increment by 2 up to 200
    print(f"Even number: {num+1}")  # Print even numbers
    time.sleep(0.5)  # Wait for 0.5 seconds

def print_odd_numbers(even_thread):
  """Function to print odd numbers from 1 to 200 while the even thread is alive."""
  i = 0
  while even_thread.is_alive():  # Continue while the even thread is alive
    print(f"Odd number: {i}")  # Print odd numbers
    i += 2
    time.sleep(0.5)  # Wait for 0.5 seconds

# Create the even thread
even_thread = threading.Thread(target=print_even_numbers)

# Create the odd thread, passing even_thread to check its status
odd_thread = threading.Thread(target=print_odd_numbers, args=(even_thread,))

# Start both threads
even_thread.start()
odd_thread.start()

# Wait for both threads to finish
even_thread.join()
odd_thread.join()

print("Both threads have finished.")
