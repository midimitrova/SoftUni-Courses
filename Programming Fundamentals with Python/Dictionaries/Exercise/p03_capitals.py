class Capitals:

    def __init__(self, countries, capitals):
        self.countries = countries
        self.capitals = capitals
        self.collect_countries_capitals = {}

    def country_and_capital(self):
        self.collect_countries_capitals = {self.countries[index]: self.capitals[index] for index in
                                           range(len(self.countries))}

    def __repr__(self):
        result = ''
        for country, capital in self.collect_countries_capitals.items():
            result += f"{country} -> {capital}\n"
        return result


country_names = input().split(', ')
capital_names = input().split(', ')
capitals = Capitals(country_names, capital_names)
capitals.country_and_capital()
print(capitals)
