import project
from input_ import Input_
from file import File_
from pyfiglet import Figlet
from person import Person
from project import Project
import bcrypt

F = Figlet(font='standard')


class User(Person):
    email = ""
    password = ""

    def __init__(self, names="", surnames="", date_birth="", hours=0, phone=""):
        super().__init__(names, surnames, date_birth, phone)
        self.name = names
        self.surnames = surnames
        self.date_birth = date_birth
        self.phone = phone
        self.hours = hours
        self.file = "users.csv"

    def input_hash_password(self):
        self.password = Input_.input_password("Introdueix una contrasenya: ")
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.password
        
    def check_password(self, input_password, hashed_password):
        if bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
        else:
            return False

    def register(self):
        name = Input_.input_text("Please enter a name: ")
        self.name = name[:1].upper() + name[1:].lower()
        surnames = Input_.input_text("Please enter a surnames: ")
        self.surnames = surnames[:1].upper() + surnames[1:].lower()
        self.date_birth = Input_.input_date("Enter date of birth: ")
        only = False
        while not only:
            self.email = Input_.input_email("Introdueix el mail: ")
            only = self.check_is_unique(self.email)
            if not only:
                print("Mail ja registrat")
        self.password = self.input_hash_password()
        print(self.password)
        self.add_user()

    def login(self):
        print(self.email, self.password, self.are_logged())
        trys = 3
        while trys > 0 and not self.are_logged():
            
            trys -= 1
            mail = Input_.input_email("Introdueix el mail: ")
            line = self.search_line(mail)
            if line != 0:
                password = Input_.input_password("Introdueix una contrasenya: ")
                user = File_.read_lines_(self.file)
                user = user[line]
                user = user.split(",")
                hashed_password = user[3]
                if self.check_password(password, hashed_password):
                    print("Login correcte")
                    self.email = mail
                    self.password = password
                    self.name = user[0]
                    self.surnames = user[1]
                    self.date_birth = user[4]
                
                else:
                    print("Login incorrecte")
            else:
                print("Mail incorrect")

        if trys == 0:
            print("Has acabat les oportunitats")

    def check_is_unique(self, email):
        users = File_.read_lines_(self.file)
        for usuari in users:
            if email in usuari:
                return False
        return True

    def search_line(self, email):
        usuaris = File_.read_lines_(self.file)
        for i in range(len(usuaris)):
            if email in usuaris[i]:
                return i
        return 0

    def are_logged(self):
        return self.email != "" and self.password != ""

    def logout(self):
        self.email = ""
        self.password = ""
        print("Logout correcte")

    def authenticator(self, options, file):
        op = Input_.input_option("Opcions vàlidas:", options)
        if op == "Registre":
            self.register()
        elif op == "Login":
            self.login()
        elif op == "Veure Projecte":
            Project.print_projects(file)

        print(F.renderText(f"Benvingut {self.name} - {self.surnames}"))

    def add_user(self):
        usuari = f"{self.name},{self.surnames},{self.email},{self.password},{self.date_birth}\n"
        File_.append_(self.file, usuari)