from getpass import getpass
from datetime import *


class Input_:
    @staticmethod
    def input_int(message, min_=0, max_=0, not_limit=True, valid_return=False):
        v = 0
        ok = False
        while not ok:
            try:
                input_value = input(message + ": ")
                if valid_return and not input_value.strip():
                    return 0

                v = int(input_value)
                if not_limit or min_ <= v <= max_:
                    ok = True

            except ValueError:
                help_ = ""
                if not_limit:
                    help_ = f" entre {min_} i {max_}"
                print("Has d'introduir un sencer " + help_ + ".")
        return v

    # Només permet lletres i espais
    @staticmethod
    def input_text(message):
        entry = input(message + ": ")
        is_valid = False
        while not is_valid:
            is_valid = all([c.isalpha() or c.isspace() for c in entry])
            if not is_valid:
                print("ERROR: Només permet lletres i espais.")
        return entry

    # Només permet un email vàlid
    @staticmethod
    def input_email(message):
        email = ""
        is_valid = False
        while not is_valid:
            email = input(message + ": ")
            is_valid = email.count("@") == 1 \
                and email.count(".") >= 1 \
                and not email.startswith("@") \
                and not email.endswith("@") \
                and not email.startswith(".") \
                and not email.endswith(".") \
                and not email.split("@")[1].startswith(".") \
                and "." in email.split("@")[1] \
                and all([c.isalpha() or c in ["@", "-", "_", "."] for c in email])

            if not is_valid:
                print("ERROR: Email invàlid.")
        return email

    # Només permet passwords de mida mínima 6, un caràcter especial, un dígit, una minúscula i una majúscula com a
    # mínim. Utilitza getpass en lloc d’input()
    @staticmethod
    def input_password(message):
        is_valid = False
        passwd = ""
        while not is_valid:
            passwd = getpass(message + ": ")
            is_valid = len(passwd) >= 6 \
                and any([c in ["@", "!", "#", "$", "%", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", ";",
                        ":", "'", "\"", "<", ">", ",", ".", "?", "/", "\\", "¡", "¿"] for c in passwd]) \
                and any([c.isdigit() for c in passwd]) \
                and any([c.isupper() for c in passwd]) \
                and any([c.islower() for c in passwd]) \

            if not is_valid:
                print("""ERROR: La contrasenya ha de complir els següents requisits:
                 · Mida mínima 6 caràcters.
                 · Mínim un caràcter especial.
                 · Mínim un dígit
                 · Mínim una minúscula. 
                 · Mínim una majúscula. 
                """)
        return passwd

    # Només permet dates en format correcte dd-mm-aaaa
    # preguntar bisi estos y 31 dias en meses de 30
    @staticmethod
    def input_date(message, mmyy=False):
        date_format = "%m-%y" if mmyy else "%d-%m-%Y"
        date_str = ""
        is_valid = False
        while not is_valid:
            date_str = input(message + ": ")
            try:
                datetime.strptime(date_str, date_format)
                is_valid = True
            except ValueError:
                if mmyy:
                    print("ERROR: Format de data incorrecte. Utilitza el format mm-yy.")
                else:
                    print("ERROR: Format de data incorrecte. Utilitza el format dd-mm-yyyy.")
        return date_str

    # Retorna True si es contesta s S y Y ok OK a un input, sinó retorna false
    @staticmethod
    def input_ok(message):
        entry = input(message)
        if entry.lower() in ["s", "y", "ok"]:
            return True
        else:
            return False

    # Donat un diccionari d’opcions, només permet una opció correcta a més afegeix l’opció 0 per sortir i retorna
    # l’opció.
    @staticmethod
    def input_option(message, options):
        leave = False
        while not leave:
            print(message)
            for key, value in options.items():
                print(f"    {key} - {value}")

            option = input("\nQue vols fer (0 per sortir)? ")

            if option == "0":
                leave = True
            elif option in options:
                return options[option]
            else:
                print("ERROR: Opció invàlida.")
        return "Sortint..."

    # Només permet la introducció de dígits, té un paràmetre num_digits que per defecte té el valor 10, retorna l’string
    # format per aquests dígits.
    @staticmethod
    def input_digits(num_digits=10):
        is_valid = False
        digits = ""
        while not is_valid:
            try:
                digits = int(input(f"Introdueix {num_digits} dígits: "))

                if len(str(digits)) == num_digits:
                    is_valid = True
                else:
                    print(f"ERROR: Has d'introduir exactament {num_digits} dígits.")

            except ValueError:
                print("ERROR: Dígits inválids.")

        return str(digits)
