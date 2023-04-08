from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, capacity=15)
        self.service_type = 'SecondaryService'

    def details(self):
        result = ''
        result += f'{self.name} Secondary Service:\n'
        robots_names = [x.name for x in self.robots]
        if robots_names:
            result += f'Robots: {" ".join(robots_names)}'
        else:
            result += f'Robots: none'

        return result
