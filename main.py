def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0:
      return x / y
  else:
      return "Error! Division by zero."

def main():
  print("Simple Calculator")

  try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
  except ValueError:
      print("Invalid input! Please enter numbers only.")
      return

  print("Choose an operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")

  operation = input("Enter the operation (+, -, *, /): ")

  if operation == '+':
      result = add(num1, num2)
  elif operation == '-':
      result = subtract(num1, num2)
  elif operation == '*':
      result = multiply(num1, num2)
  elif operation == '/':
      result = divide(num1, num2)
  else:
      print("Invalid operation! Please choose from +, -, *, /.")
      return

  print(f"The result is: {result}")

if __name__ == "__main__":
  main()
