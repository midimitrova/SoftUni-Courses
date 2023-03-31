from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GINGERBREAD_PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.GINGERBREAD_PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.GINGERBREAD_PORTION}g - {self.price:.2f}lv."
