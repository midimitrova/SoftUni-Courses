from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_TYPE_MODELS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_car_by_model(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                return True
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if self.__find_car_by_model(model):
            raise Exception(f"Car {model} is already created!")
        else:
            current_car = self.VALID_TYPE_MODELS[car_type](model, speed_limit)
            self.cars.append(current_car)
            return f"{car_type} {model} is created."

    def __find_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return True
        return False

    def create_driver(self, driver_name: str):
        if self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        else:
            current_driver = Driver(driver_name)
            self.drivers.append(current_driver)
            return f"Driver {driver_name} is created."

    def __find_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return True
        return False

    def create_race(self, race_name: str):
        if self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")
        else:
            current_race = Race(race_name)
            self.races.append(current_race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [x for x in self.drivers if x.name == driver_name][0]
        available_cars_with_required_type = [x for x in self.cars if x.__class__.__name__ == car_type and not x.is_taken]

        if not available_cars_with_required_type:
            raise Exception(f"Car {car_type} could not be found!")

        car = available_cars_with_required_type[-1]

        if driver.car:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False

            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        race = [x for x in self.races if x.name == race_name][0]

        if not self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [x for x in self.drivers if x.name == driver_name][0]

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver_name in [x.name for x in race.drivers]:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        race = [x for x in self.races if x.name == race_name][0]

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[0:3]
        result = []

        for driver in winners:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(result)

