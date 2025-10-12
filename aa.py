import random
import string

def generate_password():
    """Базовая функция генерации пароля"""
    print("Добро пожаловать в генератор паролей!")
    length = int(input("Введите длину пароля: "))
    
    # Пока просто генерируем пароль из букв
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password = generate_password()
    print(f"Ваш пароль: {password}")