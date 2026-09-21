import random
import string

def roll_dice(sides: int = 6) -> int:
    """
    Кидає кубик із заданою кількістю граней та повертає результат.
    За замовчуванням кубик має 6 граней.
    """
    return random.randint(1, sides)

def generate_password(length: int = 8) -> str:
    """
    Генерує випадковий пароль вказаної довжини.
    Пароль містить великі й малі літери, а також цифри.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
