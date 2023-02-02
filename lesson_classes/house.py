class Human:
    # Статические поля
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        """Метод инициализации экзеспляра класса
        Имеет параметры имени и возраста"""
        # Динамические поля
        # публичные
        self.name = name
        self.age = age
        # защищенный
        self._house = None
        # приватный
        self.__money = 0

    def info(self):
        """Метод выводит значения динамических полей"""
        print(
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Money: {self.__money}",
            f"House: {self._house}",
            sep="\n"
        )

    # Статический метод
    @staticmethod
    def default_info():
        """Метод выводит значения статических полей класса"""
        print(f"Default Name: {Human.default_name}")
        print(f"Age: {Human.default_age}")

    def earn_money(self, amount):
        """Метод трудовой деятельности человека
        Имеет параметр, который будет увеличивать количество денег человека"""
        self.__money += amount
        print(f"Earned {amount} money! Current value: {self.__money}")

    def __make_deal(self, house, price):
        """Приватный метод совершения покупки дома
        Имеет параметры здания и скидки на покупку"""
        self.__money -= price
        self._house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money!")


class House:
    """Класс дом, строительная компания для инициализации недвижимости"""

    def __init__(self, area, price):
        """Метод инициализации здания
        Имеет параметры площади дома и стоимость"""
        # Защищенные атрибуты класса
        self._area = area
        self._price = price

    def final_price(self, discount):
        """"Метод расчета финальной цены"""
        final_price = self._price * (100 - discount) / 100
        print(f"Final Price: {final_price}")
        return final_price


class SmallHouse(House):
    """Класс малого дома, который наследует функционал строительной компании
    Имеет условие, что площать такого дома всегда равна 40кв.м
    Имеет параметры унаследованные от класса родителя - основной класс дома
    Имеет самостоятельный параметр цены"""
    default_area = 40

    def __init__(self, price):
        """Для того чтобы наследоваться от другого класса, но не переопределить родительский метод,
        применяется функция super()"""
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":
    Human.default_info()
    alexander = Human("alexander", 27)
    alexander.info()

    small_house = SmallHouse(8500)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(5000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(4300)
    alexander.buy_house(small_house, 4)
    alexander.info()

