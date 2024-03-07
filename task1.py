from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum


@dataclass
class AllAutoDTO:
    def __init__(self, price, model, autorelease, volume):
        self.price = price
        self.model = model
        self.autorelease = autorelease
        self.volume = volume
        self.checked_out = False

    def get_full_info(self):
        return (
            f'Справочная информация: Моделечка {self.model}, {self.autorelease} года выпуска обладает {self.volume} '
            f'объемом двигателя, цена составит  {self.price} деняк.')

    def check_out(self):
        if self.checked_out:
            return f"Данной модели нет на складе/недоступна к заказу"
        else:
            self.checked_out = True
            return f"Оформляем заказ"

    def check_in(self):
        if not self.checked_out:
            return f"Данная модель доступна к заказу"
        else:
            self.checked_out = False
            return f"Оформляем возврат"


class WroomABC(ABC):
    @abstractmethod
    def run(self):
        return f'Тест-драйв in action'
        pass


class Color:
    @staticmethod
    def set_color(color):
        return f'Покрасим машину в {color} цвет.'


class Trucks(AllAutoDTO):
    def __init__(self, price, model, autorelease, volume, _capacity):
        super().__init__(price, model, autorelease, volume)
        self._capacity = _capacity


class Casual(AllAutoDTO):
    def __init__(self, price, model, autorelease, volume, _maxspeed):
        super().__init__(price, model, autorelease, volume)
        self._maxspeed = _maxspeed


class Sale(AllAutoDTO):
    def __init__(self, price, model, autorelease, volume, _cuts):
        super().__init__(price, model, autorelease, volume)
        self._cuts = _cuts

    def get_lower_price(self):
        __price2 = self.price / 100 * (100 - self._cuts)
        return f'Цена со скидкой {self._cuts} процентов составляет {__price2} деняк.'


class DisplayMixin(Color,Casual):
    def location_place(self):
        return f'Выставлена в зале'


class ColorPaletteEnum(Enum):
    color1 = 'Красный'
    color2 = 'Синий'
    color3 = 'Зеленый'
    color4 = 'Мокрый асфальт'
    color5 = 'Розовенький как у Нади'


lot1 = Casual(price=1220, model="Corolla", autorelease=24.07, volume=-0.12, _maxspeed=100500)
lot2 = Sale(price=1220, model="Corolla", autorelease=24.07, volume=-0.12, _cuts=20)
lot1.check_in()
lot1.check_out()
print(lot1.get_full_info())
print(Color.set_color('красный'))
print(lot2.get_lower_price())

for color in ColorPaletteEnum:
    print(color.value)
