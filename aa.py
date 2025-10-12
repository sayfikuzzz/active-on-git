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

import random
import string

def get_user_preferences():
    """Получаем настройки пароля от пользователя"""
    print("\n=== Настройки генератора паролей ===")
    length = int(input("Введите длину пароля: "))
    
    print("\nВыберите типы символов:")
    use_lowercase = input("Использовать строчные буквы? (y/n): ").lower() == 'y'
    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'
    
    return length, use_lowercase, use_uppercase, use_digits, use_special

def generate_password():
    """Улучшенная функция генерации пароля"""
    length, use_lower, use_upper, use_digits, use_special = get_user_preferences()
    
    # Формируем набор символов на основе выбора пользователя
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Проверяем, что выбран хотя бы один тип символов
    if not characters:
        print("Ошибка: нужно выбрать хотя бы один тип символов!")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    if password:
        print(f"\n✅ Ваш сгенерированный пароль: {password}")