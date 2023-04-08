from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPES[service_type](name)

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        robot = [x for x in self.robots if x.name == robot_name][0]

        if robot.allowed_service != service.service_type:
            return f"Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        robot = [x for x in service.robots if x.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        current_robot = [x for x in service.robots if x.name == robot_name][0]
        service.robots.remove(current_robot)
        self.robots.append(current_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(result)
