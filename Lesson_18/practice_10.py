# Lesson 18 Classwork; Task 10

# Створіть клас Temperature, який має внутрішню змінну для зберігання температури у градусах Цельсія.
# Використовуйте дескриптор для перетворення температури у градуси Фаренгейта при зверненні до атрибуту.


class Descriptor:
    def __get__(self, instance, owner):
        return instance.const * 9/5 + 32

class Convert:
    const = 20
    calc = Descriptor()

print(Convert().calc)



