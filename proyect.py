from file import File

class Proyect:

    def __init__(self, name, description, start_date, end_date, cost, id=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost
        self.status = "InProcess"
        self.id = id

    def __str__(self):
        return f"El Projecte {self.name} comença el dia {self.start_date} i acaba el dia {self.end_date}.\n{self.description}"

    def new_proyect(self):
        File.append(f"{self.id},{self.name},{self.description},{self.start_date},{self.end_date},{self.cost},{self.status}\n")