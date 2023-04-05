from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake,
    }

    VALID_DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water,
    }

    VALID_TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def __find_food_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return True
        return False

    def add_food(self, food_type: str, name: str, price: float):
        if self.__find_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.VALID_FOOD_TYPES:
            food = self.VALID_FOOD_TYPES[food_type](name, price)
            self.food_menu.append(food)

            return f"Added {name} ({food_type}) to the food menu"

    def __find_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return True
        return False

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.__find_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.VALID_DRINK_TYPES:
            drink = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)

            return f"Added {name} ({brand}) to the drink menu"

    def __find_table_by_number(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return True
        return False

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.__find_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.VALID_TABLE_TYPES:
            table = self.VALID_TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = [x for x in self.tables_repository if not x.is_reserved and x.capacity >= number_of_people][0]

        if not table:
            return f"No available table for {number_of_people} people"
        else:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        if not self.__find_table_by_number(table_number):
            return f"Could not find table {table_number}"

        table = [x for x in self.tables_repository if x.table_number == table_number][0]

        not_on_the_menu = []
        available_foods = [x.name for x in self.food_menu]

        for ordered_food in args:
            if ordered_food not in available_foods:
                not_on_the_menu.append(ordered_food)
                continue

            food = [x for x in self.food_menu if x.name == ordered_food][0]
            table.food_orders.append(food)

        result = [f"Table {table_number} ordered:"]
        for food_item in table.food_orders:
            result.append(str(food_item))

        result.append(f"{self.name} does not have in the menu:")
        for food_item in not_on_the_menu:
            result.append(food_item)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *args):
        if not self.__find_table_by_number(table_number):
            return f"Could not find table {table_number}"

        table = [x for x in self.tables_repository if x.table_number == table_number][0]

        not_on_the_menu = []
        available_drinks = [x.name for x in self.drinks_menu]

        for ordered_drink in args:
            if ordered_drink not in available_drinks:
                not_on_the_menu.append(ordered_drink)
                continue

            drink = [x for x in self.drinks_menu if x.name == ordered_drink][0]
            table.drink_orders.append(drink)

        result = [f"Table {table_number} ordered:"]
        for drink_item in table.drink_orders:
            result.append(str(drink_item))

        result.append(f"{self.name} does not have in the menu:")
        for drink_item in not_on_the_menu:
            result.append(drink_item)

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = [x for x in self.tables_repository if x.table_number == table_number][0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill

        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())

        return '\n'.join(result)

    def get_total_income(self):

        return f"Total income: {self.total_income:.2f}lv"
