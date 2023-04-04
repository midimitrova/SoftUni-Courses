from project.car.car import Car


class MuscleCar(Car):
    CAR_MIN_LIMIT = 250
    CAR_MAX_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
