import doctest


class Chair:
    def __init__(self, height: int, color: str, material: str):
        """
        Инициализирует класс Chair.

        :param height: Высота стула в сантиметрах. Должна быть положительным числом.
        :param color: Цвет стула. Должен быть не пустой строкой.
        :param material: Материал стула. Должен быть не пустой строкой.
        :raises ValueError: Если height не положителен или color/material пустые.
        :raises TypeError: Если height не число.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(height, int):
            raise TypeError("Высота должена быть типа int")
        if not color or not isinstance(color, str):
            raise ValueError("Цвет должен быть не пустой строкой")
        if not material or not isinstance(material, str):
            raise ValueError("Материал должен быть не пустой строкой")

        self.height = height
        self.color = color
        self.material = material

    def repaint(self, new_color: str) -> None:
        """
        Перекрашивает стул в новый цвет.

        :param new_color: Новый цвет стула. Должен быть не пустой строкой.
        :raises ValueError: Если new_color пустая строка.
        :return: None
        >>> chair = Chair(100, "Красный", "Дерево")
        >>> chair.repaint("Синий")
        >>> chair.color
        'Синий'
        """
        if not new_color or not isinstance(new_color, str):
            raise ValueError("Новый цвет должен быть не пустой строкой")
        self.color = new_color
        ...

    def move(self, new_height: int) -> None:
        """
        Переставляет стул на новую высоту.

        :param new_height: Новая высота стула в сантиметрах. Должна быть положительным числом.
        :raises ValueError: Если new_height не положителен.
        :raises TypeError: Если new_height не число типа int.
        :return: None
        >>> chair = Chair(100, "Красный", "Дерево")
        >>> chair.move(90)
        >>> chair.height
        90
        """
        if new_height <= 0:
            raise ValueError("Новая высота должна быть положительным числом")
        if not isinstance(new_height, int):
            raise TypeError("Высота должена быть типа int")
        self.height = new_height
        ...


class LightBulb:
    def __init__(self, color: str, lifespan: int, size: float):
        """
        Инициализирует класс LightBulb.

        :param color: Цвет лампочки. Должен быть не пустой строкой.
        :param lifespan: Срок действия лампочки в часах. Должен быть положительным целым числом.
        :param size: Размер лампочки в сантиметрах. Должен быть положительным числом.
        :raises ValueError: Если color пустая строка, lifespan не положителен или size не положителен.
        :raises TypeError: Если lifespan не число или size не число.
        """
        if not color or not isinstance(color, str):
            raise ValueError("Цвет должен быть не пустой строкой")
        if not isinstance(lifespan, int):
            raise TypeError("Срок действия лампочки должен быть типа int")
        if lifespan <= 0:
            raise ValueError("Срок действия лампочки должен быть положительным числом")
        if not isinstance(size, float):
            raise TypeError("Размер должен быть типа float")
        if size <= 0:
            raise ValueError("Размер должен быть положительным числом")

        self.color = color
        self.lifespan = lifespan
        self.size = size
        self.is_on = False  # Лампочка выключена по умолчанию

    def turn_on(self) -> None:
        """
        Включает лампочку.

        :return: None
        >>> bulb = LightBulb("теплый белый", 1000, 10.0)
        >>> bulb.turn_on()
        >>> bulb.is_on
        True
        """
        self.is_on = True
        ...

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет лампочки.

        :param new_color: Новый цвет лампочки. Должен быть не пустой строкой.
        :raises ValueError: Если new_color пустая строка.
        :return: None
        >>> bulb = LightBulb("теплый белый", 1000, 10.0)
        >>> bulb.change_color("холодный белый")
        >>> bulb.color
        'холодный белый'
        """
        if not new_color or not isinstance(new_color, str):
            raise ValueError("New color must be a non-empty string.")
        self.color = new_color
        ...


class SocialNetwork:
    def __init__(self, friends_count: int, subscriptions_count: int):
        """
        Инициализирует класс SocialNetwork.

        :param friends_count: Количество друзей. Должен быть неотрицательным целым числом.
        :param subscriptions_count: Количество подписок. Должен быть неотрицательным целым числом.
        :raises ValueError: Если friends_count или subscriptions_count отрицательны.
        :raises TypeError: Если friends_count или subscriptions_count не числа типа int.
        """
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным")
        if not isinstance(friends_count, int):
            raise TypeError("Количество друзей должно быть типа int")
        if subscriptions_count < 0:
            raise ValueError("Количество подписок не может быть отрицательным")
        if not isinstance(subscriptions_count, int):
            raise TypeError("Количество подписок должно быть типа int")

        self.friends_count = friends_count
        self.subscriptions_count = subscriptions_count

    def add_friend(self) -> None:
        """
        Добавляет нового друга.

        :return: None
        >>> sn = SocialNetwork(10, 5)
        >>> sn.add_friend()
        >>> sn.friends_count
        11
        """
        self.friends_count += 1
        ...

    def subscribe_to_group(self) -> None:
        """
        Подписывается на новую группу.

        :return: None
        >>> sn = SocialNetwork(10, 5)
        >>> sn.subscribe_to_group()
        >>> sn.subscriptions_count
        6
        """
        self.subscriptions_count += 1
        ...


if __name__ == "__task 1__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
