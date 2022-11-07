class CompanyUsers:

    def __init__(self):
        self.company_data = {}

    def collect_data(self, company_name: str, employee_id: str):
        if company_name not in self.company_data.keys():
            self.company_data[company_name] = []
        if employee_id not in self.company_data[company_name]:
            self.company_data[company_name].append(employee_id)


company_users = CompanyUsers()
data = input()
while data != 'End':
    company, employee_id = data.split(' -> ')
    company_users.collect_data(company, employee_id)
    data = input()

for company, employee in company_users.company_data.items():
    print(f"{company}")
    for id in company_users.company_data[company]:
        print(f"-- {id}")
