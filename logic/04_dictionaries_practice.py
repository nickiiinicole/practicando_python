
#ejercicio basico de diccionarios 
def show_person():
    person= {
        'name': 'nicki',
        'age': 20,
        'city': 'Vigo'
    }

    print(person.values())
    student ={
        'name': 'nicki',
        'mark':8
    }
    student['curse']='Python'
    print(student.pop('curse'))
    print(student)
    
# Pide al usuario una frase y crea un diccionario donde las claves sean las palabras
# y los valores sean el número de veces que aparece cada palabra.
def count_words():

    phrase = input("Please enter a phrase: ")
    words= phrase.split()
    counter_words={}
    for word in words:
        if word in counter_words.keys():
            counter_words[word]+=1
        else:
            counter_words[word]=1
    print(counter_words)

# Crea un programa que pida nombres y notas de varios alumnos hasta que el usuario escriba "fin".
# Guárdalos en un diccionario y muestra:

# La nota media

# Qué alumno tiene la nota más alta

def school_marks():
    students = {}
    name = ""

    print("Write 'fin' to finish.\n")
    while name.lower() != "fin":
        name = input("Please enter the student's name: ")
        if name.lower() != "fin":
            mark = float(input("Please enter the student's mark (1–10): "))
            if 1 <= mark <= 10:
                students[name] = mark
            else:
                print("Please enter a valid mark (1–10).")
    if len(students) == 0:
        print("No students entered.")
        return
    marks = list(students.values())
    average = sum(marks) / len(marks)
    max_mark = max(marks)
    best_students = [name for name, mark in students.items() if mark == max_mark]

    print("\nResults:")
    print(f"Average mark: {average:.2f}")
    print(f"Highest mark: {max_mark}")
    print("Best student(s):", ", ".join(best_students))
# {'Ana': 8.5, 'Brais': 9}

# Invertir un diccionario

# Dado un diccionario {"A": 1, "B": 2, "C": 3},
# crea otro diccionario donde las claves sean los valores y los valores sean las claves.
# Resultado esperado: {1: "A", 2: "B", 3: "C"}

def reverse(dictionary_to_reverse):
    #esto dict comprehension impte-> forma corta de crear diciionarios usando bulce dentro {}
    # {clave: valor for elemento in iterable}
    dictionary_reverse = {v: k for k, v in dictionary_to_reverse.items()}
    return dictionary_reverse

# ** -> disctionary unpacking
# tab hay este para las tuplas *
#sirve para extraer todas las clave-valor y las pega dentro de otro
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

combi = {**a, **b}
print(combi)
# el resultado es este : {'x': 1, 'y': 3, 'z': 4}
