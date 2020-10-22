import itertools
import time
class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 4))
    def running(self):
        for color, sec in itertools.cycle(self.__color):
            print(color)
            time.sleep(sec)
tf = TrafficLight()
tf.running()


