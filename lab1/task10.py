"""
10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, 
знайти кількість повних кілобайтів, які займає даний файл(1 кілобайт=1024 байта)
"""


def bite_to_kilobytes(a: int) -> int:
    return(a / 1024)


print("Enter a positive number")
a = int(input("a = "))
print(int(bite_to_kilobytes(a)))
