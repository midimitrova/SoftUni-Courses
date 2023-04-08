from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=7)
        self.robot_type = 'FemaleRobot'
        self.allowed_service = "SecondaryService"

    def eating(self):
        self.weight += 1
