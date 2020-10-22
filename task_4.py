class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going!')

    def stop(self):
        print(f'{self.name} is stopping!')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} is turning to {direction}!')

    def show_speed(self):
        print('Current speed:', self.speed)

class TownCar(Car):
    def show_speed(self):
        print(('Current speed:', self.speed))
        if self.speed > 60:
            print('Attantion, lower your speed ')

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Attantion, lower your speed ')
class PoliceCar(Car):
    pass
town_car = TownCar('городская машина ',100,'белая', False)
work_car = WorkCar('рабочая машина ', 70, 'серая', False)
sport_car = SportCar('спортивная  машина ', 200, 'красная', False)
police_car = PoliceCar('полицейская машина ', 150, 'белосиняя', True)
town_car.go()
sport_car.turn('right')
work_car.show_speed()
police_car.stop()
