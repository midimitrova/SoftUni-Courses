from abc import ABC, abstractmethod


class Car(ABC):
    CAR_MIN_LIMIT = None
    CAR_MAX_LIMIT = None

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self.CAR_MIN_LIMIT <= value <= self.CAR_MAX_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {self.CAR_MIN_LIMIT} and {self.CAR_MAX_LIMIT}!")

        self.__speed_limit = value
