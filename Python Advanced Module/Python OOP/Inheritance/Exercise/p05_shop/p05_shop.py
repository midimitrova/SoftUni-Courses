from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
repo.remove('juice')
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
