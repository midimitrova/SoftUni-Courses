from project.animal import Animal


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care = 0
        for animal in self.animals:
            total_care += animal.money_for_care
        if self.__budget >= total_care:
            self.__budget -= total_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ''
        result += f"You have {len(self.animals)} animals\n"
        result += self.__build_entity_counter(self.animals, 'Lion')
        result += self.__build_entity_counter(self.animals, 'Tiger')
        result += self.__build_entity_counter(self.animals, 'Cheetah')
        return result.strip()

    def workers_status(self):
        result = ''
        result += f"You have {len(self.workers)} workers\n"
        result += self.__build_entity_counter(self.workers, 'Keeper')
        result += self.__build_entity_counter(self.workers, 'Caretaker')
        result += self.__build_entity_counter(self.workers, 'Vet')
        return result.strip()

    def __build_entity_counter(self, entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result
