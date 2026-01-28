n = 4
for i in range(1, n + 1):
    print("*" * i)

# *
# **
# ***
# ****

n = 4
for i in range(n, 0, -1):
    print("*" * i)
# ****
# ***
# **
# *

n = 4
for i in range(1, n + 1):
    espacios = n - i
    print(" " * espacios + "*" * i)


#    *
#   **
#  ***
# ****


n = 4
for i in range(n):
    espacios = n - i - 1
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

#    *
#   ***
#  *****
# *******

n = 4
for i in range(n - 1, -1, -1):
    espacios = n - i - 1
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

# *******
#  *****
#   ***
#    *
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 1
# 12
# 123
# 1234


n = 4
for i in range(1, n + 1):
    print(str(i) * i)

# 1
# 22
# 333
# 4444

n = 4
for i in range(1, n + 1):
    espacios = n - i
    izquierda = "".join(str(x) for x in range(1, i))
    derecha = "".join(str(x) for x in range(i, 0, -1))
    print(" " * espacios + izquierda + derecha)

#    1
#   121
#  12321
# 1234321

n = 4
for i in range(n):
    for j in range(2 * n - 1):
        if (
            j == n - i - 1 or
            j == n + i - 1 or
            i == n - 1
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#    *
#   * *
#  *   *
# *******

# con while
i = 1
n = 4
while i <= n:
    print("*" * i)
    i += 1

# *
# **
# ***
# ****
