# Global constants (UPPERCASE and with_underscores)
PI = 3.14159
PACIO_DEV = 'https://pacio.dev'

print("Without global keyword:")
enemies = 1

def increase_enemies():
    enemies = 2
    print(f'    Enemies inside function: {enemies}') # 2

increase_enemies()
print(f'    Enemies outside function: {enemies}') # 1

print("-------------------------------------")
print("With global keyword:")
print("-------------------------------------")

enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f'    Enemies inside function: {enemies}') # 2

increase_enemies()
print(f'    Enemies outside function: {enemies}') # 2