from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([
        {'signal': 'red', 'duration': 7},
        {'signal': 'yellow', 'duration': 2},
        {'signal': 'green', 'duration': 5},
        {'signal': 'yellow', 'duration': 2}
    ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['signal']}, переключение через {light['duration']} сек.")
        sleep(light['duration'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()