
def division():
    """функция выводящая результат деления на ноль"""
    try:
        divider = int(input("Введите число"))
        num = int(input("Введите делитель"))
        return f"{num} / {divider} = {num / divider}"
    except ZeroDivisionError: #отлов ошибки деления на ноль
        return "нельзя делить на ноль"

print(division())
