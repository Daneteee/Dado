from pyfiglet import Figlet
import bcrypt

F = Figlet(font='standard')

class Usuari(Persona):
    email = ""
    password = ""
    

    def __init__(self, names="", surnames="", date_birth="", hours=0):
        super().__init__(names, surnames, date_birth, phone)
        self.name = names
        self.surnames = surnames
        self.date_birth = date_birth
        self.phone = phone
        self.hours = hours
        self.file = "users.csv"

    def input_hash_password(self):
        self.password = Input_.input_password("Please enter a password: ")
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
        self.date_birth = Input_.input_data("Enter date of birth: ")
        only = False
        while not only:
            self.email = Input_.input_email("Please enter a mail: ")
            only = self.check_is_unique(self.email)
            if not only:
                print("Mail already registred")
        self.password = self.input_hash_password()
        print(self.password)
        self.add_user()

    def login(self):
        print(self.email, self.password, self.are_logged())
        trys = 3
        while trys > 0 and not self.are_logged():
            
            trys -= 1
            mail = Input_.input_email("Please enter a mail: ")
            line = self.search_line(mail)
            if line != 0:
                password = Input_.input_password("Please enter a password: ")
                user = Arxiu.llegir_linies(self.file)
                user = user[line]
                user = user.split(",")
                hashed_password = user[3]
                if self.check_password(password, hashed_password):
                    print("Login correct")
                    self.email = mail
                    self.password = password
                    self.name = user[0]
                    self.surnames = user[1]
                    self.date_birth = user[4]
                
                else:
                    print("Login incorrect")
            else:
                print("Mail incorrect")
                
            

        if trys == 0:
            print("You've run out of opportunities")

    
    def check_is_unique(self, email):
        usuaris = Arxiu.llegir_linies(self.file)
        for usuari in usuaris:
            if email in usuari:
                return False
        return True

    def search_line(self, email):
        usuaris = Arxiu.llegir_linies(self.file)
        for i in range(len(usuaris)):
            if email in usuaris[i]:
                return i
        return 0

    def are_logged(self):
        return self.email != "" and self.password != ""

    def logout(self):
        self.email = ""
        self.password = ""
        print("Logout correct")

    def autenticator(self):
        print("You need to identify yourself, are you new? register or else login")
        sortir = False
        while not self.are_logged() and not sortir:
            opcio = {"r": "Register", "l": "Login"}
            op = Input_.input_opcio(opcio)
            if op == "Registre":
                self.register()
            elif op == "Login":
                self.login()
            elif op == "Sortir":
                sortir = True

        print(F.renderText(f"Welcome {self.name} - {self.surnames}"))

    def add_user(self):
        usuari = f"{self.name},{self.surnames},{self.email},{self.password},{self.date_birth}\n"
        Arxiu.afegir(self.file, usuari)
    
