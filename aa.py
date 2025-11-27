import random
import string
import re
from datetime import datetime

def generate_password():
    """Базовая функция генерации пароля"""
    print("Добро пожаловать в генератор паролей!")
    length = int(input("Введите длину пароля: "))
    # Пока просто генерируем пароль из букв
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

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
    print(f"Ваш пароль: {password}")
    
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

if __name__ == "__main__":
    password = generate_password()
    if password:
        print(f"\n✅ Ваш сгенерированный пароль: {password}")
        
def evaluate_password_strength(password):
    """Оценивает сложность пароля"""
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Длина пароля хорошая")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️  Пароль средней длины")
    else:
        feedback.append("❌ Пароль слишком короткий")
    
    # Проверяем наличие разных типов символов
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Определяем уровень сложности
    if score >= 5:
        strength = "Очень сильный"
    elif score >= 3:
        strength = "Сильный"
    elif score >= 2:
        strength = "Средний"
    else:
        strength = "Слабый"
    
    feedback.append(f"🏆 Уровень сложности: {strength} (очков: {score}/6)")
    return strength, feedback

def generate_password():
    """Функция генерации пароля с оценкой сложности"""
    length, use_lower, use_upper, use_digits, use_special = get_user_preferences()
    
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("Ошибка: нужно выбрать хотя бы один тип символов!")
        return None
        
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Оцениваем сложность пароля
    strength, feedback = evaluate_password_strength(password)
    
    return password, strength, feedback

if __name__ == "__main__":
    result = generate_password()
    if result:
        password, strength, feedback = result
        print(f"\n🔐 Ваш сгенерированный пароль: {password}")
        print("\n".join(feedback))



def save_passwords_to_file(passwords, filename="passwords.txt"):
    """Сохраняет пароли в текстовый файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"=== Сгенерированные пароли ===\n")
            file.write(f"Дата создания: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 40 + "\n\n")
            
            for i, (password, strength, _) in enumerate(passwords, 1):
                file.write(f"Пароль #{i}:\n")
                file.write(f"Пароль: {password}\n")
                file.write(f"Сложность: {strength}\n")
                file.write("-" * 30 + "\n")
        
        print(f"✅ Пароли сохранены в файл: {filename}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при сохранении файла: {e}")
        return False

def generate_multiple_passwords():
    """Генерирует несколько паролей"""
    print("\n=== Генератор нескольких паролей ===")
    
    try:
        num_passwords = int(input("Сколько паролей сгенерировать? "))
        length, use_lower, use_upper, use_digits, use_special = get_user_preferences()
        
        characters = ""
        if use_lower:
            characters += string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            print("Ошибка: нужно выбрать хотя бы один тип символов!")
            return None
        
        passwords = []
        for i in range(num_passwords):
            password = ''.join(random.choice(characters) for _ in range(length))
            strength, feedback = evaluate_password_strength(password)
            passwords.append((password, strength, feedback))
        
        # Показываем результаты
        print(f"\n=== Сгенерировано {num_passwords} паролей ===")
        for i, (password, strength, feedback) in enumerate(passwords, 1):
            print(f"\n🔐 Пароль #{i}: {password}")
            print(f"🏆 Сложность: {strength}")
        
        # Предлагаем сохранить в файл
        save_choice = input("\n💾 Сохранить пароли в файл? (y/n): ").lower()
        if save_choice == 'y':
            filename = input("Введите имя файла (или нажмите Enter для passwords.txt): ").strip()
            if not filename:
                filename = "passwords.txt"
            save_passwords_to_file(passwords, filename)
        
        return passwords
        
    except ValueError:
        print("❌ Ошибка: введите корректное число!")
        return None

def main():
    """Главная функция программы"""
    print("🎯 Генератор безопасных паролов")
    print("=" * 40)
    
    while True:
        print("\nВыберите действие:")
        print("1 - Сгенерировать один пароль")
        print("2 - Сгенерировать несколько паролей")
        print("3 - Выйти")
        
        choice = input("Ваш выбор (1-3): ").strip()
        
        if choice == '1':
            result = generate_password()
            if result:
                password, strength, feedback = result
                print(f"\n🔐 Ваш пароль: {password}")
                print("\n".join(feedback))
        
        elif choice == '2':
            generate_multiple_passwords()
        
        elif choice == '3':
            print("👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор, попробуйте снова.")


