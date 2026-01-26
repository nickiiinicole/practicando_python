
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEjercicio 1:")
number = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
if number>number2:
    print(f"The greater number is: {number}")
elif number2>number:
    print(f"The greater number is: {number2}")
else:
    print(f"Both numbers are equal")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nEjercicio 2:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

result = None

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: You can't divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operation.")

if result is not None:
    print(f"The result is: {result:.2f}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nExercise 3: Leap Year Checker:)")

year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nExercise 4: Age Checker:)")
input_valid = False
while not input_valid:
    age = int(input("Please enter ur age: ")) 
    if age<0 :
        print("Please enter valid age")  
    else:
        input_valid = True

if 0<= age <=2:
    print(f"BABY")
elif 3<= age <= 12:
    print("KID")
elif 13<= age <= 17:
    print("TEENAGER")
elif 18<=age<=64:
    print("ADULT")
else:
    print("SENIOR:,)")