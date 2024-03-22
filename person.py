from datetime import datetime


class Person:
    def __init__(self, name, last_name, date_birth, phone):
        self.name = name
        self.last_name = last_name
        self.date_born = date_birth
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.date_born}"

    def user_ago(self):
        date_now = datetime.now()
        data_usu = datetime.strptime(self.date_born, "%d-%m-%Y")
        date_now_date = date_now.date()
        operation = date_now_date - data_usu.date()
        total_years = round(operation.days / 365)
        print(f"Age in years to {self.name}, {self.last_name}: {total_years}")
        return total_years

    def is_major(self):
        if self.age_usu() >= 18:
            return True
        else:
            return False
