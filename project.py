from file import File_
from prettytable import *


class Project:
    def __init__(self, name, description, start_date, category, end_date="NoLimit", id=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.category = category
        self.status = "InProcess"
        self.id = id

    def __str__(self):
        return f"El Projecte {self.name} comença el dia {self.start_date} i acaba el dia {self.end_date}.\n{self.description}"

    def new_project(self, file):
        File_.append_(file, f"{self.id},{self.name},{self.description},{self.start_date},{self.end_date},{self.category},{self.status}\n")

    def update_status(self, status):
        self.status = status

    def update_project(self, file):
        f_lines = File_.read_lines_(file)
        for i in range(len(f_lines)-1):
            if f_lines[i+1].split(",")[0] == self.id:
                f_lines[i+1] = f"{self.id}, {self.name}, {self.description}, {self.start_date}, {self.end_date}, {self.category}, {self.status}\n"
        File_.write_lines_(f_lines)

    def delete_project(self, file):
        f_lines = File_.read_lines_(file)
        for i in range(len(f_lines)-1):
            if f_lines[i+1].split(",")[0] == self.id:
                f_lines.pop(i+1)
        File_.write_lines_(f_lines)

    @staticmethod
    def print_projects(file):
        f_lines = File_.read_lines_(file)
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Descripcio", "Durada", "Categoria", "Estatus"]
        for n_line in range(len(f_lines)-1):
            line = f_lines[n_line+1].split(",")
            table.add_row([line[0], line[n_line][1], line[n_line][2], f"{line[3]} - {line[4]}", line[5], line[6]])

            print(table) if (n_line+1) % 20 == 0 or n_line == len(f_lines) - 1 else None
            table.clear_rows() if (n_line+1) % 20 == 0 or n_line == len(f_lines) - 1 else None
            input() if (n_line+1) % 20 == 0 else None
