from project.car.car import Car


class SportsCar(Car):
    CAR_MIN_LIMIT = 400
    CAR_MAX_LIMIT = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
