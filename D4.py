
class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Cтоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(f"Тест-драйв {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("Поездка завершена", end="\n\n")



polo = TownCar('черный', 'Volkswagen Polo')
test_drive(polo)

ferrari = SportCar('красный', 'Ferrari')
test_drive(ferrari)

kamaz = WorkCar('синий', 'KAMAZ')
test_drive(kamaz)

ford = PoliceCar('белый', 'Ford')
test_drive(ford)






