from lib import roll_dice, generate_password

def main():
    """
    Головна функція, яка демонструє роботу генератора паролів та кидання кубика.
    """
    print("=== Демонстрація роботи модулів ===")
    
    # 1. Кидання кубика
    sides = 20
    dice_result = roll_dice(sides)
    print(f"🎲 Ви кинули {sides}-гранний кубик і випало число: {dice_result}")
    
    # 2. Генерація пароля
    pass_length = 12
    new_password = generate_password(pass_length)
    print(f"🔑 Ваш новий згенерований пароль (довжина {pass_length}): {new_password}")
    
    print("===================================")

if __name__ == "__main__":
    main()
