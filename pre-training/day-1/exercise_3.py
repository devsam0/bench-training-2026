def run_multiplication_generator():
  while True:
    try:
      user_input = int(input("Enter a number (1-12) for the table: "))
      if 1 <= user_input <= 12:
        break
      print("Out of range. Please stay between 1 and 12.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  print(f"\nMultiplication Table for {user_input}:")
  for i in range(1, 13):
    print(f"{user_input:>2} x {i:>2} = {user_input * i:>3}")

# All tables
def print_all_tables():
  print("\n--- Full 1-12 Master Table ---")
  for row in range(1, 13):
    for col in range(1, 13):
      print(f"{row * col:>4}", end=" ")
    print()

run_multiplication_generator()
# Uncomment the line below to run the bonus
# print_all_tables()
